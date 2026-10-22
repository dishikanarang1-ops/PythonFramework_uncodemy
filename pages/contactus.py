class cl_contact_us:
    def __init__(self, page):
        self.page = page
        self.contact_us_link = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.name_input = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email_input = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.company_input = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service_dropdown = page.locator('(//select[@name="service"])[2]')
        self.phone_input = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message_textarea = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit_button = page.locator('(//input[@type="submit"])[2]')
        self.service_options = [
            page.locator('//a[contains(normalize-space(.), "CMS Website Development")]'),
            page.locator('//a[contains(normalize-space(.), "eCommerce Development")]'),
            page.locator('//a[contains(normalize-space(.), "Custom Web Portal Development")]'),
            page.locator('//a[contains(normalize-space(.), "iOS App Development")]'),
            page.locator('//a[contains(normalize-space(.), "Android App Development")]'),
            page.locator('//a[contains(normalize-space(.), "Hybrid Mobile App Development")]'),
            page.locator('//a[contains(normalize-space(.), "Cross-Platform App Development")]'),
            page.locator('//a[contains(normalize-space(.), "Progressive Web App Development")]'),
            page.locator('//a[contains(normalize-space(.), "Logo Design")]'),
            page.locator('//a[contains(normalize-space(.), "Banner Design")]'),
            page.locator('//a[contains(normalize-space(.), "Packaging Design")]'),
            page.locator('//a[contains(normalize-space(.), "Business cards Design")]'),
        ]

    def contact_us_option(self):
        self.contact_us_link.click()

    def fill_contact_details(self, contact_data):
        self.name_input.fill(contact_data["name"])
        self.email_input.fill(contact_data["email"])
        self.company_input.fill(contact_data["company"])
        self.service_dropdown.select_option(label=contact_data["service"])
        self.phone_input.fill(contact_data["phone"])
        self.message_textarea.fill(contact_data["message"])
        self.submit_button.click()
