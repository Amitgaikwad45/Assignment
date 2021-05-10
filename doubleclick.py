from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://www.tutorialspoint.com/index.htm")
driver.maximize_window()

element=driver.find_element_by_xpath("//*[text()='GATE Exams']")

actions=ActionChains(driver)
actions.double_click(element).perform()
driver.close()
