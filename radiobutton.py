from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')


driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')


status=driver.find_element_by_xpath("//label[@for='RESULT_RadioButton-7_0']").click()
print(status)



