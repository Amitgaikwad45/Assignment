from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')


driver.get('http://www.google.com')
#implicit wait
driver.implicitly_wait(10)
assert "Google" in driver.title
ele=driver.find_element_by_name("btnK")
print(ele.is_displayed())
print(ele.is_enabled())
driver.close()
driver.quit()