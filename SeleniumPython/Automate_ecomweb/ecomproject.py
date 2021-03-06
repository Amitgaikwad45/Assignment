from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
import random

driver=webdriver.Chrome(executable_path='E:/chromedriver.exe')

driver.get('http://www.tutorialsninja.com/demo/')
driver.maximize_window()

#phone button
phones=driver.find_element_by_xpath('//a[text()="Phones & PDAs"]')
phones.click()

#iphone
iphone=driver.find_element_by_xpath('//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

#first picture
first_pic=driver.find_element_by_xpath('//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

#next picture
next_click=driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')

for i in range(0,5):
    next_click.click()
    time.sleep(2)

#save screenshot
driver.save_screenshot('screenshot#'+str(random.randint(0,101))+'.png')

x_btn=driver.find_element_by_xpath('//button[@title="Close (Esc)"]')
x_btn.click()
time.sleep(1)

#quantity
qty=driver.find_element_by_id('input-quantity')
qty.click()
time.sleep(1)

qty.clear()
time.sleep(1)
qty.send_keys('2')
time.sleep(2)

#add to cart
add_to_btn=driver.find_element_by_id('button-cart')
add_to_btn.click()

#select laptop
laptop=driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver)
action.move_to_element(laptop).perform()
time.sleep(2)
laptop2=driver.find_element_by_xpath('//a[text()="Show All Laptops & Notebooks"]')
laptop2.click()
time.sleep(1)

#click on HP laptop
HP=driver.find_element_by_xpath('//a[text()="HP LP3065"]')
HP.click()

#scroll
add_to_btn1=driver.find_element_by_xpath('//button[@id="button-cart"]')
add_to_btn1.location_once_scrolled_into_view
time.sleep(1)

#calendar
calendar=driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

#selecting given year
next_click_calendar=driver.find_element_by_xpath('//th[@class="next"]')
month_year=driver.find_element_by_xpath('//th[@class="picker-switch"]')
while month_year.text != 'December 2022':
    next_click_calendar.click()
time.sleep(2)

#selecting given date
calendar_date=driver.find_element_by_xpath('//td[text()="31"]')
calendar_date.click()
time.sleep(2)

#add to button
add_to_btn1.click()
time.sleep(1)

#checkout
go_to_cart=driver.find_element_by_id('cart-total')
go_to_cart.click()
time.sleep(1)

checkout=driver.find_element_by_xpath('//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

ship_tax=driver.find_element_by_xpath('//a[text()="Estimate Shipping & Taxes "]')
ship_tax.click()
time.sleep(1)

#country
country=driver.find_element_by_id('input-country')
dropdown=Select(country)
time.sleep(1)
dropdown.select_by_visible_text('Brazil')
time.sleep(1)

#region
region=driver.find_element_by_id('input-zone')
dropdown1=Select(region)
time.sleep(1)
dropdown1.select_by_visible_text('Bahia')
time.sleep(1)

#postalcode
postalcode=driver.find_element_by_id('input-postcode')
postalcode.click()
time.sleep(1)
postalcode.send_keys('111222')
time.sleep(2)

#final price
price=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/table/tbody/tr[4]/td[2]')
print("final price of all the products"+price.text)

#continue shopping
continue_shop=driver.find_element_by_xpath('//a[text()="Continue Shopping"]')
continue_shop.click()

driver.close()
