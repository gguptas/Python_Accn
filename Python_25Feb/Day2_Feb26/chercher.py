from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

menu = driver.find_element_by_id("sub-menu")
google_link = driver.find_element_by_id("link2")

actions = ActionChains(driver)
actions.move_to_element(menu).move_to_element(google_link).click(google_link).perform()
driver.back()
actions1 = ActionChains(driver)
double_click99=driver.find_element_by_id("double-click")
actions1.double_click(double_click99).perform()
alert = driver.switch_to_alert()
str1=alert.text
print(str1)
alert.accept()