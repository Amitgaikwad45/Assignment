from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium import webdriver
class LoginPage(BasePage):
    """By locators"""
    EMAIL=(By.ID,"txtUsername")
    PASSWORD=(By.ID,"txtPassword")
    LOGIN_BUTTON=(By.ID,"btnLogin")
    SIGNUP_LINK=(By.ID,"logInPanelHeading")

    """constructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions for login page"""

    
    def get_login_page_title(self,title):
        #This is used to get the page title
        return self.get_title(title)

    
    def is_signup_link_exist(self):
        #This is used to check the signup link
        return self.is_visible(self.SIGNUP_LINK)

    
    def do_login(self,username,password):
        #This is used to login into the page
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)


