import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='F:/chromedriver.exe')

driver.get('https://swayamopenid.b2clogin.com/swayamopenid.onmicrosoft.com/B2C_1_swayam2/oauth2/v2.0/authorize?response_type=code&client_id=019220f4-2ec0-41c2-a727-529f1b54bb06&redirect_uri=https%3A%2F%2Fswayam.gov.in%2Fwso_ok&scope=https%3A%2F%2Fswayamopenid.onmicrosoft.com%2Fapi%2Fuser_impersonation+offline_access+openid&state=4CnKdeVtRNj0MfBXWjYZGPyyaTxBvQ&access_type=authorization_code')
path="F:/login.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)


driver.find_element_by_xpath("//*[@id='logonIdentifier']").send_keys(username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
driver.find_element_by_id("next").click()

if driver.title=="Swayam Central":
    print("test passed")
    XLUtils.writeData(path,"Sheet1",r,3,"test passed")
else:
    print("test failed")
    XLUtils.writeData(path, "Sheet1", r, 3, "test failed")


    driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul/li[1]/a").click()
