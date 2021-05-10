from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get('http://www.google.com')
driver.maximize_window()
driver.find_element_by_name("q").send_keys("types of inheritance in java")
time.sleep(3)

#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//input[@aria-label='Google Search']").click()
time.sleep(3)
driver.quit()
print("sample test case successfully completed")


