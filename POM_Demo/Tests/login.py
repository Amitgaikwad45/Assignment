from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from POM_Demo.Pages.login_page import LoginPage
from POM_Demo.Pages.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.driver=webdriver.Chrome(executable_path='E:/WebAutomationPython3/drivers/chromedriver.exe')
            cls.driver.implicitly_wait(10)
            cls.driver.maximize_window()

        def test_01_login_valid(self):
            driver=self.driver
            driver.get("https://opensource-demo.orangehrmlive.com/")
            login=LoginPage(driver)
            login.enter_username("Admin")
            login.enter_password("admin123")
            login.click_login()
            homepage=HomePage(driver)
            homepage.click_welcome()
            homepage.click_screenshot()
            homepage.click_logout()
            time.sleep(2)

            #test for invalid credentials
        def test_02_login_invalid_cred(self):
            driver=self.driver
            driver.get("https://opensource-demo.orangehrmlive.com/")
            login=LoginPage(driver)
            login.enter_username("Admin1")
            login.enter_password("admin123")
            login.click_login()
            #creating Homepage class object
            homepage=HomePage(driver)
            homepage.click_welcome()
            homepage.click_screenshot()
            homepage.click_logout()
            #returning value from function
            val=driver.find_element_by_xpath("").text
            #using assertion compare values of expected result and actual result
            self.assertEqual(val,"Invalid credentials123")
            time.sleep(2)



        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/WebAutomationPython3/reports'))
