from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create a new chromedriver instance
driver = webdriver.Chrome(executable_path='F:/chromedriver.exe')

# Go to www.google.com
driver.get("https://www.google.com")

try:
    # Wait as long as required, or maximum of 5 sec for element to appear
    # If successful, retrieves the element
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "q")))

    # Type "selenium"
    element.send_keys("selenium")

    # Type Enter
    element.send_keys(Keys.ENTER)

except TimeoutException:
    print("Failed to load search bar at www.google.com")
finally:
    driver.quit()