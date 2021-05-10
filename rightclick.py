from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
driver.maximize_window()
#to refresh the browser
driver.refresh()
# identifying the source element
source= driver.find_element_by_xpath("//*[text()='Company']");
# action chain object creation
action = ActionChains(driver)
# right click operation and then perform
action.context_click(source).perform()
#to close the browser
driver.close()