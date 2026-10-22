import pytest

from pages.technologies import technologies


@pytest.mark.smoke
def test_technologies(page):
    obj=technologies(page)
    obj.technologies_clicking()

@pytest.mark.smoke
def test_technologies_mad(page):
    obj=technologies(page)
    obj.technologies_mad_clicking()


@pytest.mark.smoke
def test_ai(page):
    obj=technologies(page)
    obj.technologies_ai_click()