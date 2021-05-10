from selenium import  webdriver
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')


driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("webDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("org.openqa.selenium").click()
driver.switch_to.default_content()