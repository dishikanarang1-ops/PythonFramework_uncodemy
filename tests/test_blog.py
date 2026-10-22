import pytest
from playwright.sync_api import expect
from pages.blog import cl_blog

def test_blog_options(page):
    blog_opt = cl_blog(page)
    page.wait_for_load_state("load")
    blog_opt.blog.click()
    page.wait_for_load_state("load")

    blog_url = page.url

    for option in blog_opt.blog_options:
        assert option.count() > 0, "Blog option was not found"
        blog_option = option.last
        expected_url = blog_option.get_attribute("href")
        print (expected_url)
        assert expected_url, "Blog option has no URL"

        blog_option.click()
        page.wait_for_load_state("load")
        assert page.url != blog_url, "Blog option did not navigate"
        page.go_back()
        page.wait_for_load_state("load")


def test_blog_horizontal_menu(page):
    blog_opt = cl_blog(page)
    blog_opt.blog.click()
    page.wait_for_load_state("load")

    blog_url = page.url

    for option in blog_opt.horizontal_menu_options:
        assert option.count() > 0, "Horizontal menu option was not found"
        menu_option = option.last
        expected_url = menu_option.get_attribute("href")
        print (expected_url)
        assert expected_url, "Horizontal menu option has no URL"
        expect(menu_option).to_be_visible()
        expect(menu_option).to_be_enabled()

        menu_option.click()
        page.wait_for_load_state("load")
        assert expected_url in page.url, f"Wrong URL: {page.url}"
        page.go_back()
        page.wait_for_load_state("load")


