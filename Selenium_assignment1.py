#program 2
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='F:/chromedriver.exe')

# Go to www.google.com
driver.get("https://www.flightradar24.com/data/airports/pnq")

driver.maximize_window()

rows = 1 + len(driver.find_elements_by_xpath(
    "/html/body/div[6]/div[2]/section/div/section/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[11]"))

#cols = len(driver.find_elements_by_xpath(
#    "/html/body/div[6]/div[2]/section/div/section/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[11]/td"))
f_id1=driver.find_element_by_xpath("//html/body/div[6]/div[2]/section/div/section/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[12]/td[2]/a").text
f_city1=driver.find_element_by_xpath("//*[@id='cnt-data-content']/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[12]/td[3]/div[1]/span").text
f_stat1=driver.find_element_by_xpath("//*[@id='cnt-data-content']/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[12]/td[7]/span").text


f_id2=driver.find_element_by_xpath("/html/body/div[6]/div[2]/section/div/section/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[13]/td[2]/a").text
f_city2=driver.find_element_by_xpath("//*[@id='cnt-data-content']/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[13]/td[3]/div[1]/span").text
f_stat2=driver.find_element_by_xpath("//*[@id='cnt-data-content']/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[13]/td[7]/span").text


print(f_id2)
print(f_city2)
print(f_stat2)


d1 = defaultdict(list)
d1 = {
    'f1': [f_id1,f_city1, f_stat1],
    'f2': [f_id2,f_city2,f_stat2]
}
print(d1['f1'])
for k in d1:
    print(k,d1.get(k))
    
    
print(rows)
#print(cols)

# Printing the data of the table
#for r in range(1, rows + 1):
   # for p in range(1, cols + 1):
        # obtaining the text from each column of the table
     #   value = driver.find_element_by_xpath(
      #      "/html/body/div[6]/div[2]/section/div/section/div/div[2]/div/aside[1]/div[1]/table/tbody/tr[r]/td[p]").text
       # print(value, end='       ')
    #print()
