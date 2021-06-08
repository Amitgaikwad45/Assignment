

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    HEADER=(By.TAG_NAME,"h1")
    UID=(By.ID,"welcome")
    MARKETPLACE=(By.ID,"MP_link")


    def __init__(self,driver):
        #calling parent class constructor
        super().__init__(driver)
        

    def get_home_page_title(self,title):
        #method returns title of the page
        return self.get_title(title)

    def is_user_icon_exist(self):
        # return true if icon exist else return false
        return self.is_visible(self.UID)

    def get_header_value(self):
        #checks the element is visible or not if visibile return text associated with that element
        if  self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_marketplace_value(self):
    # checks the element is visible or not if visibile return text associated with that element
        if  self.is_visible(self.MARKETPLACE):
            return self.get_element_text(self.MARKETPLACE)
