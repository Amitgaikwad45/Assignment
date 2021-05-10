from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin=driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/a/b")
usermgmt=driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a")
users=driver.find_elements_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a")


actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()#error

