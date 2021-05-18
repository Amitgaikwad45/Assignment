
from selenium.webdriver.common.by import By
from POM_Demo.Locators.locators import Locators
class HomePage():

    def __init__(self,driver):
        self.driver=driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_text = "Logout"
        self.path = "C:/Users/amit.g/Pictures/Saved Pictures/page.png"

    def click_welcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def click_screenshot(self):
        self.driver.save_screenshot(self.path)

    def click_logout(self):
        #method to click logout button
        self.driver.find_element_by_link_text(self.logout_link_text).click()
