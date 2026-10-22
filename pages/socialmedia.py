class socialmedia:
    def __init__(self, page):
        self.page=page
        self.about=page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        self.facebook=page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin=page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.insta=page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pin=page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter=page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.youtube=page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.quora=page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')
