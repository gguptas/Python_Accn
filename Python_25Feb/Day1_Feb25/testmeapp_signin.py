'''
Created on Feb 25, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/RegisterUser.htm")
driver.find_element_by_name("userName").send_keys("shojghjgjhgj")
driver.find_element_by_name("firstName").send_keys("Testing")
driver.find_element_by_id("lastName").send_keys("Singh")
driver.find_element_by_id("password").send_keys("andompassword12")
driver.find_element_by_id("pass_confirmation").send_keys("andompassword12")
driver.find_element_by_id("emailAddress").send_keys("testingmail@wxyz.com")
driver.find_element_by_id("mobileNumber").send_keys("1234567897")
driver.find_element_by_id("dob").send_keys("12/23/1989")
driver.find_element_by_id("address").send_keys("Just a random address of awesome personality")
driver.find_element_by_xpath("//input[@value='Female']").click()
select = Select(driver.find_element_by_name('securityQuestion'))
select.select_by_visible_text('What is your Pet Name?')
time.sleep(2)
select.select_by_value("411012")
driver.find_element_by_id("answer").send_keys("Delhi")
driver.find_element_by_name("Submit").click()