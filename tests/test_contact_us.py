import pytest
from pages.contactus import cl_contact_us

# def test_contactusform(page, contact_data):

#     contact = cl_contact_us(page)
#     page.wait_for_load_state("load")
#     contact.contact_us_option()
#     page.wait_for_timeout(5000)
#     contact.fill_contact_details(contact_data)
#     page.wait_for_timeout(5000)


def test_contact_service_options(page):
    contact = cl_contact_us(page)
    contact.contact_us_option()
    page.wait_for_load_state("load")
    contact_url = page.url
    failures = []

    for option in contact.service_options:
        # Always start each iteration from the Contact Us page.
        page.goto(contact_url)
        page.wait_for_load_state("load")

        assert option.count() > 0, "Service option was not found on Contact Us page"
        option = option.last
        expected_url = option.get_attribute("href")

        if not expected_url:
            failures.append("Service option has no URL")
            continue

        try:
            option.click()
            page.wait_for_load_state("load")
            if expected_url not in page.url:
                message = f"FAILED: expected {expected_url}, opened {page.url}"
                print(message)
                failures.append(message)
            else:
                print(f"PASSED: {expected_url}")
        except Exception as error:
            message = f"FAILED: {expected_url}: {error}"
            print(message)
            failures.append(message)

    assert not failures, "Service option failures:\n" + "\n".join(failures)
    
