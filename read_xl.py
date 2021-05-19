#datadriven testing
import XUtils
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
   # ele=driver.find_element_by_xpath("//div[@id='logInPanelHeading']")
    driver.find_element_by_id("btnLogin").click()

    if driver.title=='OrangeHRM' :
        print("test passed")
        XUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test failed")
        XUtils.writeData(path,"Sheet1",r,3,"test failed")

    #go back to login page for next iteration
    driver.find_element_by_id("welcome").click()
    el=driver.find_element_by_link_text("Logout")
    el.click()