from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(10)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(10)

highest = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
highest.select_by_value("hilo")
time.sleep(5)
items =driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
print(len(items))
items[0].click()
driver.window_handles()

time.sleep(5)
driver.close()



