from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get("https://accounts.google.com/signup")

driver.find_element_by_link_text("Help").click()

#prints parent window title
print("Parent window title: " + driver.title)

#get current window handle
p = driver.current_window_handle

#get first child window
ch = driver.window_handles
for w in ch:
#switch focus to child window
    if(w!=p):
        driver.switch_to.window(w)
        break
time.sleep(0.9)
print("Child window title: " + driver.title)
print(driver.current_url)
driver.quit()