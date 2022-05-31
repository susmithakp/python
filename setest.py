from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import xlrd
import time
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
#WebDriverWait(driver, 10)
time.sleep(5)
#element_name = driver.find_element(By.ID, "Form_submitForm_Name")
element_name= driver.find_element(By.XPATH, "//input[contains(@name, 'Name')]")
element_email = driver.find_element(By.ID, "Form_submitForm_Email")
element_phone = driver.find_element(By.ID, "Form_submitForm_Contact")
element_country = Select(driver.find_element(By.ID, "Form_submitForm_Country"))


#loc = "/Users/susmitha/Documents/orangedata.xls"
info = xlrd.open_workbook("/Users/susmitha/Documents/selenium_python/testdata.xls")
sheet = info.sheet_by_name("Sheet 1")
rowcount = sheet.nrows
colcount = sheet.ncols
print(rowcount)
print(colcount)
for curr_row in range(2, rowcount):
    name = sheet.cell_value(curr_row,0)
    email = sheet.cell_value(curr_row,1)
    phone = sheet.cell_value(curr_row,2)
    country = sheet.cell_value(curr_row,3)

    element_name.send_keys(name)
    element_email.send_keys(email)
    element_phone.send_keys(phone)
    element_country.select_by_value(country)
#element_country.find_elements(By.TAG_NAME, country)
#for option in all_options:
    #print("Value is: %s" % option.get_attribute(country))

    time.sleep(5)

    element_name.clear()
    element_email.clear()
    element_phone.clear()

    #driver.findElement(By.className("alert-content"));
    message = driver.find_element(By.XPATH, "//span[contains(@class,'description js-validator')]")
    actual_error = message.get_attribute('innerHTML')
    Expected_error= "wrong message"
    if actual_error == Expected_error:
        print("test passed")
    else:
        print("test not passed")
        print(actual_error)

driver.close()
