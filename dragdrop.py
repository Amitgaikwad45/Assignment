


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')







driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
#to refresh the browser
driver.refresh()
# identifying the source and target elements
source= driver.find_elements(By.ID,'draggable')
target= driver.find_elements(By.ID,'droppable')
# action chain object creation
action = ActionChains(driver)
# drag and drop operation and the perform
action.drag_and_drop(source, target).perform()
