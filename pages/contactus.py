# class cl_contact_us:
#     def __init__(self, page):
#         self.page = page
#         self.contact_us_link = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
#         self.name_input = page.locator('(//input[@placeholder="Your Name"])[2]')
#         self.email_input = page.locator('(//input[@placeholder="Your Mail"])[2]')
#         self.company_input = page.locator('(//input[@placeholder="Your Company"])[2]')
#         self.service_dropdown = page.locator('(//select[@name="service"])[2]')
#         self.phone_input = page.locator('(//input[@placeholder="Your Phone"])[2]')
#         self.message_textarea = page.locator('(//textarea[@placeholder="Message"])[2]')
#         self.submit_button = page.locator('(//input[@type="submit"])[2]')
#         self.service_options = [
#             page.locator('//a[contains(normalize-space(.), "CMS Website Development")]'),
#             page.locator('//a[contains(normalize-space(.), "eCommerce Development")]'),
#             page.locator('//a[contains(normalize-space(.), "Custom Web Portal Development")]'),
#             page.locator('//a[contains(normalize-space(.), "iOS App Development")]'),
#             page.locator('//a[contains(normalize-space(.), "Android App Development")]'),
#             page.locator('//a[contains(normalize-space(.), "Hybrid Mobile App Development")]'),
#             page.locator('//a[contains(normalize-space(.), "Cross-Platform App Development")]'),
#             page.locator('//a[contains(normalize-space(.), "Progressive Web App Development")]'),
#             page.locator('//a[contains(normalize-space(.), "Logo Design")]'),
#             page.locator('//a[contains(normalize-space(.), "Banner Design")]'),
#             page.locator('//a[contains(normalize-space(.), "Packaging Design")]'),
#             page.locator('//a[contains(normalize-space(.), "Business cards Design")]'),
#         ]

#     def contact_us_option(self):
#         self.contact_us_link.click()

#     def fill_contact_details(self, contact_data):
#         self.name_input.fill(contact_data["name"])
#         self.email_input.fill(contact_data["email"])
#         self.company_input.fill(contact_data["company"])
#         self.service_dropdown.select_option(label=contact_data["service"])
#         self.phone_input.fill(contact_data["phone"])
#         self.message_textarea.fill(contact_data["message"])
#         self.submit_button.click()


class contact:
    def __init__(self,page):
        self.page=page
        self.trank=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/logo/trank-logo.webp"]')
        #CONTACTUS
        self.contact=page.locator('(//a[text()="Contact us"])[1]')
        self.name=page.locator('(//input[@name="name"])[2]')
        self.email=page.locator('(//input[@name="email"])[2]')
        self.otp=page.locator('(//button[@type="button"])[2]')
        self.enter_otp=page.locator('(//input[@name="otp"])[2]')
        self.company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.phone=page.locator('(//input[@name="phone"])[2]')
        self.message=page.locator('(//textarea[@name="message"])[2]')
        self.frame=page.frame_locator('(//iframe[@role="presentation"])[2]')
        self.captcha=self.frame.locator('(//label[@id="recaptcha-anchor-label"])[1]')
        self.submit=page.locator('(//input[@type="submit"])[2]')

    def contact_information(self):
        self.contact.click()
        self.name.fill("Dishika")
        self.email.fill("dishikan@gmail.com")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.otp.click()
        self.enter_otp.fill("1234567")
        self.company.fill("abc")
        self.service.select_option("Web Development")
        self.phone.fill("1234567890")
        self.message.fill("Learning Playwright Automation")
        self.submit.click()

    def trank_tech(self):
        self.trank.click()

