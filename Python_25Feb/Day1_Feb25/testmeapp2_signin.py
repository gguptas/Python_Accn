'''
Created on Feb 25, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.find_element_by_link_text("REGISTER").click()

driver.find_element_by_name("firstName").send_keys("Testing")
driver.find_element_by_name("lastName").send_keys("Singh")
driver.find_element_by_name("phone").send_keys("1234567897")
driver.find_element_by_name("userName").send_keys("testing@gmail.com")

driver.find_element_by_name("address1").send_keys("some good and real address")
driver.find_element_by_name("city").send_keys("cityname")
driver.find_element_by_name("state").send_keys("statename")
driver.find_element_by_name("postalCode").send_keys("110098")


select = Select(driver.find_element_by_name('country'))
select.select_by_visible_text('BELGIUM')
time.sleep(2)
select.select_by_value("BELGIUM")

driver.find_element_by_name("email").send_keys("random")
driver.find_element_by_name("password").send_keys("test123")
driver.find_element_by_name("confirmPassword").send_keys("test123")
driver.find_element_by_name("submit").click()