from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("file:///E:/demo.html")
#driver.maximize_window()
#rows=driver.find_element_by_xpath("/html/body/table/tbody/tr")#count number of rows
rw=driver.find_elements(By.TAG_NAME,"tr")
cols=driver.find_elements(By.TAG_NAME,"th")
t=len(rw)

x=int(t)+1
p=len(cols)
y=int(p)+1
print(len(cols))
print(len(rw))
for i in range(2,x):
    for j in range(1,y):
            val=driver.find_element_by_xpath("/html/body/table/tbody/tr[i]/td["+str(j)+"]").text
            print(val)
        print()