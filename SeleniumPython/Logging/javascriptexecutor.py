from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:/chromedriver.exe')
driver.get('https://classic.crmpro.com/')
driver.implicitly_wait(7)
# best_seller=driver.find_element(By.LINK_TEXT,'Best Sellers')
# driver.execute_script("arguments[0].click();",best_seller)
#
# title=driver.execute_script("return document.title;")
# print(title)
#
#
# #to refresh the page
# driver.execute_script("history.go(0);")
#
# #alert
# driver.execute_script("alert('hello selenium')")
#
# #to print all content of the page
# inner_text=driver.execute_script("return document.documentElement.innerText;")
# print(inner_text)
#
#to make border to webelement
#form=driver.find_element(By.ID,'hs-login')
#driver.execute_script("arguments[0].style.border = '3px solid red'",form)

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
forgot_pwd=driver.find_element(By.LINK_TEXT,'Forgot Password?')
driver.execute_script("arguments[0].scrollIntoView(true);",forgot_pwd)

#print useragent
print(driver.execute_script("return navigator.userAgent;"))
driver.execute_script("document.getElementById('username').value='abc@gmail.com';")



