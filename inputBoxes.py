from selenium import  webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')


driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print(status)
driver.find_element(By.ID,'RESULT_TextField-1').send_keys("abc")

driver.find_element(By.ID,'RESULT_TextField-2').send_keys("xyz")

driver.find_element(By.ID,'RESULT_TextField-3').send_keys("3333333333")
