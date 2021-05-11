# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.chrome.options import Options
#download at specified location
#chromeOptions=Options()
#chromeOptions.add_experimental_option("pref",{"download.default_directory":"C:\Downloadfiles"})
#driver=webdriver.Chrome(executable_path='F:/chromedriver.exe',chrome_options="chromeOptions")

driver=webdriver.Chrome(executable_path='F:/chromedriver.exe')

# Open URL
driver.get(
	'http://demo.automationtesting.in/FileDownload.html')

# Enter text
driver.find_element_by_id('textbox').send_keys("Hello world")

# Generate Text File
driver.find_element_by_id('createTxt').click()

# Click on Download Button
driver.find_element_by_id('link-to-download').click()
#download pdf file
driver.find_element_by_id('pdfbox').send_keys("testing pdf")
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()
#driver.close()