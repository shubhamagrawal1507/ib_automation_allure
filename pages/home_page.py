from playwright.sync_api import Page

class HomePage:

    def __init__(self, page:Page):
        self.page = page
        self.logo = page.locator("//a[@title='Logo Menu']")
        self.navbar_options = page.locator("//ul[@id='menu-main-menu']//li//h5")
        self.btn_contact_us = page.locator("//a[@title='Contact Us']")

    def get_all_navbar_options(self):
        options = []
        self.page.wait_for_timeout(timeout=3000)
        for option in self.navbar_options.all():
            options.append(option.inner_text())
        return options
    
    def get_embedded_link(self,button_name):
        if button_name == "CONTACT US":
            self.page.wait_for_timeout(timeout=3000)
            return self.btn_contact_us.get_attribute("href")

    

