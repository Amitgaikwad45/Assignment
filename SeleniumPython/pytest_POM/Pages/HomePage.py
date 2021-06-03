
from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    HEADER=(By.TAG_NAME,"h1")
    UID=(By.ID,"welcome")
    MARKETPLACE=(By.ID,"MP_link")


    def __init__(self,driver):
        super().__init__(driver)
        #self.driver.get(TestData.BASE_URL)

    def get_home_page_title(self,title):
        return self.get_title(title)

    def is_user_icon_exist(self):
        return self.is_visible(self.UID)

    def get_header_value(self):
        if  self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_marketplace_value(self):
        if  self.is_visible(self.MARKETPLACE):
            return self.get_element_text(self.MARKETPLACE)
