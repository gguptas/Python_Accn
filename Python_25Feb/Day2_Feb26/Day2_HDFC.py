from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.maximize_window()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.switch_to_frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("1234567898")
driver.find_element_by_xpath("//img[@value='Continue']").click() 
driver.switch_to_default_content()
driver.switch_to_frame(1)
driver.find_element_by_link_text("Privacy Policy").click()
driver.maximize_window()