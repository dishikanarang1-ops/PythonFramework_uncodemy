from datetime import datetime
from pathlib import Path
import re
import shutil
from uuid import uuid4

import pytest
from playwright.sync_api import sync_playwright

from config import BASE_URL


REPORTS_DIR = Path(__file__).parent / "reports"
VIDEOS_DIR = REPORTS_DIR / "videos"


def _safe_filename(value):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")



@pytest.fixture(autouse=True)
def page(request):
    """Record every pytest test in its own fresh browser context."""
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    video_name = _safe_filename(request.node.nodeid) or "test"
    execution_id = uuid4().hex
    video_path = VIDEOS_DIR / f"{video_name}-{execution_id}.webm"
    raw_video_dir = VIDEOS_DIR / f".recording-{execution_id}"
    raw_video_dir.mkdir()

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(raw_video_dir),
        record_video_size={"width": 1280, "height": 720},
    )
    test_page = context.new_page()

    try:
        test_page.goto(BASE_URL)
        test_page.wait_for_load_state("load")
        yield test_page
    finally:
        # Playwright finalizes the video when its page/context is closed.
        video = test_page.video
        try:
            test_page.close()
            context.close()
            if video is not None:
                video.save_as(str(video_path))
                request.node._playwright_video_path = video_path
        finally:
            browser.close()
            playwright.stop()
            shutil.rmtree(raw_video_dir, ignore_errors=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # Fixture teardown (which finalizes the recording) is complete by the
    # teardown report hook, so attach the video there.
    if report.when != "teardown":
        return

    video_path = getattr(item, "_playwright_video_path", None)
    if video_path is None or not video_path.exists():
        return

    extras = getattr(report, "extras", [])
    try:
        import pytest_html
    except ImportError:
        # Videos remain available in reports/videos even without pytest-html.
        return

    relative_video = Path("videos") / video_path.name
    extras.append(pytest_html.extras.url(relative_video.as_posix(), name="Execution video"))
    report.extras = extras
