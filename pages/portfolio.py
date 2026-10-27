class portfolio:
    def __init__(self,page):
        self.page=page
        self.trank=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/logo/trank-logo.webp"]')
        self.port_folio=page.locator('//a[text()="Portfolio"]')
        self.ics_homework=page.locator('(//a[text()="View More"])[1]')
        self.wings_pharma=page.locator('(//a[text()="View More"])[2]')
        self.arena_animation=page.locator('(//a[text()="View More"])[3]')
        self.home_360=page.locator('(//a[text()="View More"])[4]')
        self.club_meeting=page.locator('(//a[text()="View More"])[5]')
        self.cord_cables=page.locator('(//a[text()="View More"])[6]')

    def portfolio_viewmore_clicking(self):
            self.port_folio.click()
            self.page.wait_for_load_state(state="load")
            self.portfolio_list=[self.ics_homework,self.wings_pharma,self.arena_animation,
                                 self.home_360,self.cord_cables]
            for portfolio_viewmore in self.portfolio_list:
                with self.page.context.expect_page() as new_page_info:
                    portfolio_viewmore.click()
                new_tab=new_page_info.value
                new_tab.wait_for_load_state("load")
                new_tab.close()

    def trank_tech(self):
            self.trank.click()

        