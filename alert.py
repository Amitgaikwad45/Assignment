from selenium import  webdriver
import time

from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm')

driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()

driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
time.sleep(5)
