from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/downloads/")
#driver.find_element_by_link_text("API Docs").click()
driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[2]/td[6]/a[4]").click()  
driver.switch_to_frame("classFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
time.sleep(4)
driver.switch_to_default_content()
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(4)
driver.switch_to_default_content()
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("OutputType").click()