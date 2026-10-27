# from urllib.parse import urlparse

# import pytest

# from pages.socialmedia import socialmedia

# @pytest.mark.smoke
# def test_social_media_links(page):
#     social = socialmedia(page)

#     # Click About
#     # social.about.click()
#     page.wait_for_load_state("load")

#     # List of social media locators
#     social_media_list = [
#         (social.facebook, "facebook.com"),
#         (social.linkedin, "linkedin.com"),
#         (social.insta, "instagram.com"),
#         (social.pin, "pinterest.com"),
#         (social.twitter, "twitter.com"),
#         (social.youtube, "youtube.com"),
#         (social.quora, "quora.com"),
#     ]

#     # Verify each social media link opens in a new tab
#     for social_media_link, expected_domain in social_media_list:
#         with page.context.expect_page() as new_page_info:
#             social_media_link.click()

#         new_tab = new_page_info.value
#         new_tab.wait_for_load_state("domcontentloaded")

#         # Verify the tab opened the expected social media website.
#         hostname = urlparse(new_tab.url).hostname or ""
#         expected_domains = (expected_domain, "x.com") if expected_domain == "twitter.com" else (expected_domain,)
#         assert any(
#             hostname == domain or hostname.endswith(f".{domain}")
#             for domain in expected_domains
#         )

#         # Close the new tab
#         new_tab.close()


import pytest
from pages.socialmedia import socialmedia
from pages.socialmedia import socialmedia

@pytest.mark.smoke
def test_socialmedia(page):
    obj=socialmedia()
    obj.socialmediapageclick()



























