#datadriven testing
import XUtils
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='F:/chromedriver.exe')
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

path="F:/datadriven.xlsx"
rows=XUtils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    #first column gives username and second gives password
    username=XUtils.readData(path,"Sheet1",r,1)
    password=XUtils.readData(path,"Sheet1",r,2)


    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    if driver.current_url=='https://opensource-demo.orangehrmlive.com/index.php/dashboard' :
        print("test passed")
        XUtils.writeData(path,"Sheet1",r,3,"test passed")
        driver.find_element_by_id("welcome").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[3]/a").click()
    else:
        print("test failed")
        XUtils.writeData(path,"Sheet1",r,3,"test failed")

    #go back to login page for next iteration


driver.close()
