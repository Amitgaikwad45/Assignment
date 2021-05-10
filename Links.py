from selenium import  webdriver
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('https://www.geeksforgeeks.org/')
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))#print nummber of links present in a page

for i in links:
    print(i.text)

#clicking on text link
#driver.find_element(By.LINK_TEXT,"Java Tutorial").click()#pass exact link text

