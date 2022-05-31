#from login import *
#import login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
check=driver.find_element(By.XPATH, "//a[text()='\"Company \"']")
check.click()
#driver.find_element(By.LINK_TEXT, "Company").click()
#driver.find_element(By.XPATH("//a[@href='/orangehrm-30-day-trial/?#']")).click()
time.sleep(10)
driver.quit()
