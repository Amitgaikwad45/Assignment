from selenium import  webdriver
from time import sleep

driver=webdriver.Chrome(executable_path='E:/chromedriver.exe')
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(2)

def searchplace():
    place=driver.find_element_by_class_name("tactile-searchbox-input")
    place.send_keys("Tiruchirapalli")
    submit=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]")
    submit.click()

searchplace()


def directions():
    sleep(10)
    direction=driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div/button/img")
    direction.click()
directions()

def find():
    sleep(5)
    find=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    find.send_keys("Tirunelveli")
    sleep(5)
    search=driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()

find()

def kmeters():
    sleep(5)
    tkm=driver.find_element_by_xpath("//*[@id='section-directions-trip-1']/div/div[1]/div[1]/div[2]/div")
    print("total distance ",tkm.text)
    driver.close()

kmeters()