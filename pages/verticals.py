class verticals:
    def __init__(self,page):
#hover items
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('(//img[@alt="trading"])[1]')
        self.retail_and_ecommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.healthcare=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.fintech_mobile_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.custom_App=page.locator('//strong[text()="Custom App"]')
#vertical Options:    
    #vertical--> Trading:
        self.Stock_trading=page.locator('(//a[text()="Stock Trading"])[1]')
        self.algo_Trading=page.locator('(//a[text()="Algo Trading"])[1]')
        self.paper_trading=page.locator('(//a[text()="Paper Trading"])[1]')
        self.custom_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_Trading=page.locator('(//a[text()="CFD Trading"])[1]')
        self.webportal_trading=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.stock_trading_development_massachusetts=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.vertical_Trading=[self.Stock_trading,self.algo_Trading,self.paper_trading,self.custom_trading,self.cfd_Trading,self.webportal_trading,self.stock_trading_development_massachusetts]
    #vertical : Retail and Ecommerce
        self.ecommerce_web_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecommerce_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retailAndEcommerce=[self.ecommerce_web_development,self.ecommerce_app_development]
    
    #Vertical : Healthcare
        #healthcare=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]').click()
        self.diet_n_nutrition_app=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health_tracking_app=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthcare_list=[self.diet_n_nutrition_app,self.health_tracking_app]
    
    #Vertical : fintech
    #fintech-mobile-app-development=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.pos_software=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintech_list=[self.pos_software,self.crypto]

    #Vertical :Custom_App
    #custom_App=pos-software-development-company=page.locator('(//a[text()="Custom App")[1]').hover()
        self.desktop_application_development=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm_development_company=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm_application=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel_mobile_app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.e_learning_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating_app=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.real_estate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.custom_crm_development=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.custom_list=[self.desktop_application_development,self.crm_development_company,self.hrm_application,self.erp_app_development,self.travel_mobile_app_development,self.e_learning_mobile,
                 self.dating_app,self.real_estate,self.custom_crm_development]


    def trading_options_clicking(self):
        for i in self.vertical_Trading:
            self.vertical.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    #vertical : Retail and Ecommerce
    def retail_ecommerce_clicking(self):
        for i in self.retailAndEcommerce:
            self.vertical.hover()
            self.retail_and_ecommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    
    def healthcare_clicking(self):
        for i in self.healthcare_list:
            self.vertical.hover()
            self.healthcare.hover()        
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()  

    def fintech_clicking(self):
        for i in self.fintech_list:
            self.vertical.hover()
            self.fintech_mobile_app_development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def custom_App_clicking(self):
        for i in self.custom_list:
            self.vertical.hover()
            self.custom_App.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()



        



    

