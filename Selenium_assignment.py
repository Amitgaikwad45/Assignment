from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='F:/chromedriver.exe')
driver.get("http://www.google.com")
driver.maximize_window()
try:
    element = driver.find_element_by_name("q");
    element.send_keys("selenium hq");
    element.submit();

except:
    print("not found")


f=0
for r in range(1,10):
    results = driver.find_elements_by_xpath("//h3[text()='Selenium (software) - Wikipedia']")

    for re in results:
        if(re.text=='Selenium (software) - Wikipedia'):
            #r.click()
            ele=driver.find_element_by_xpath("//div[@class='IsZvec']/span[@class='aCOpRe']/span[contains(text(),'is a portable frame')]")
            print(ele.text)
            f=1
            break
    if(f==1):
        break
    else:
        driver.find_element_by_xpath("// *[ @ id = 'pnnext'] / span[2]").click()
driver.close()

