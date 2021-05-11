from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path='F:/chromedriver.exe')

driver.get('https://www.geeksforgeeks.org/')
driver.maximize_window()
#capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))
#print all cookie pairs
print(cookies)
#add new cookie to browser
cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)#print number of cookies after adding new one

#deleting the cookie
driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies))#after deleting the cookie print the count
#delete all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))