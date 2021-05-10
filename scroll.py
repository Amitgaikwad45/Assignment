from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#scroll down by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#scroll down till element visible
#flg=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flg)

#scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
