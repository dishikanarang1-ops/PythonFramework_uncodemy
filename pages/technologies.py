class technologies:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.eCommerce=page.locator('(//strong[text()="eCommerce Development"])[1]')
        self.magento=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.opencart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.codeigniter=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.wordpress=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.big_commerce=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.shopify=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.cs_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.node_js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.nopcommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.woocommerce=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.laravel=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.prestashop=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.drupal=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.wix=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.joomla=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.react_js=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.express=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ecomm_list=[self.magento,self.opencart,self.codeigniter,self.wordpress,self.big_commerce,self.shopify,self.cs_cart,self.node_js,self.nopcommerce,self.woocommerce,self.laravel,self.prestashop,self.drupal,self.wix,
                self.joomla,self.react_js,self.express]

        self.mad=page.locator('(//strong[text()="Mobile App Development"])[1]')
        self.react=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_mobil_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarin=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appointment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobile=[self.react,self.enterprise_mobil_dev,self.xamarin,self.kotlin,self.flutter,self.ionic,self.swift,self.appointment]
        self.ai=page.locator('(//strong[text()="Artificial Intelligence"])[1]') 
        


    def technologies_clicking(self):
        for i in self.ecomm_list:
            self.technologies.hover()
            self.eCommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()


    def technologies_mad_clicking(self):
        for i in self.mobile:
            self.technologies.hover()
            self.mad.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
        
    def technologies_ai_click(self):
        self.technologies.hover()
        self.ai.click()
        self.page.go_back()
        #self.page.wait_for_timeout(5000)