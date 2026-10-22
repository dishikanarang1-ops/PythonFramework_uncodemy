import pytest

from pages.socialmedia import socialmedia

@pytest.mark.smoke
def test_social_media_links(page):
    social = socialmedia(page)

    # Click About
    # social.about.click()
    page.wait_for_load_state("load")

    # List of social media locators
    social_media_list = [
        (social.facebook, "facebook.com"),
        (social.linkedin, "linkedin.com"),
        (social.insta, "instagram.com"),
        (social.pin, "pinterest.com"),
        (social.twitter, "twitter.com"),
        (social.youtube, "youtube.com"),
        (social.quora, "quora.com"),
    ]

    # Verify each social media link opens in a new tab
    for social_media_link, expected_domain in social_media_list:
        with page.context.expect_page() as new_page_info:
            social_media_link.click()

        new_tab = new_page_info.value
        new_tab.wait_for_load_state("domcontentloaded")

        # Verify the tab opened the expected social media website.
        assert expected_domain in new_tab.url

        # Close the new tab
        new_tab.close()




