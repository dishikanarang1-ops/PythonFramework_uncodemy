class cl_blog:
    def __init__(self, page):
        self.page = page
        # self.blog = page.locator('//a[@href ="https://www.tranktechnologies.com/blog/"][1]')
        self.blog = page.locator("//a[text() = 'Blog']").first
        self.appdev = page.locator('//a[contains(text(), "App Development")]')
        self.webdev = page.locator('//a[contains(text(), "Web Development")]')
        self.softwaredev = page.locator('//a[contains(text(), "Software Development")]')
        self.digitalmarketing = page.locator('//a[contains(text(), "Digital Marketing")]')
        self.emailmarketing = page.locator('//a[contains(text(), "Email Marketing")]')
        self.ai = page.locator('//a[contains(text(), "Artificial Intelligence")]')
        self.uiux = page.locator('//a[contains(text(), "UI UX Design")]')

        self.blog_options = [
            self.appdev,
            self.webdev,
            self.softwaredev,
            self.digitalmarketing,
            self.emailmarketing,
            self.ai,
            self.uiux,
        ]

        # Horizontal menu displayed below the main navigation.
        self.horizontal_menu_options = [
            page.locator('//a[contains(text(), "App Development")]'),
            page.locator('//a[contains(text(), "Web Development")]'),
            page.locator('//a[contains(text(), "Software Development")]'),
            page.locator('//a[contains(text(), "Digital Marketing")]'),
            page.locator('//a[contains(text(), "Email Marketing")]'),
            page.locator('//a[contains(text(), "Artificial Intelligence")]'),
            page.locator('//a[contains(text(), "UI UX Design")]'),
        ]


