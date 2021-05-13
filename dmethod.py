#from selenium import webdriver


#driver = webdriver.Chrome(executable_path='F:/chromedriver.exe')



#driver.implicitly_wait(0.5)
#driver.get("https://www.tutorialspoint.com/index.htm")
# to identify element and obtain text
#s = driver.find_element_by_css_selector("h4").text
#print("The text is: " + s)
from selenium import webdriver
driver = webdriver.Chrome(executable_path="F:/chromedriver.exe")
driver.implicitly_wait(0.5)
driver.get("https://www.tutorialspoint.com/tutor_connect/index.php")
#identify element with attribute id
l= driver.find_element_by_xpath("//input[@id='txtSearchText']")
l.send_keys("Tutorialspoint")
#get_attribute() to get value of input box
print("Enter text is: " + l.get_attribute('value'))
#find the name started with title New User Register
s = driver.find_element_by_css_selector("a[title*='New User Register']").text
print("The text is: " + s)

