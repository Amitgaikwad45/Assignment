
from POM_Demo.Locators.locators import Locators
class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        #Adding objects
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = "btnLogin"
        self.invalid_cred_message="//span[@id='spanMessage']"

    def enter_username(self,username):
        #clearing the textbox value first
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        #clearing initial value of password field
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)


    def click_login(self):
         self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_cred_message(self):
        msg=self.driver.find_element_by_xpath(self.invalid_cred_message).text
        return msg
