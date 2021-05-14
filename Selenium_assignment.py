#program 1
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='F:/chromedriver.exe')

# Go to www.google.com
driver.get("https://www.google.com")

driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("selenium hq")
#driver.find_element(By.NAME,"btnK").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()

element=driver.find_element_by_xpath("//*[@id='rso']/div[8]/div/div/div[2]/span/span").text
#element=driver.find_element_by_id('rso').text
print(element)







