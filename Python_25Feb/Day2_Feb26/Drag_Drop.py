from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\python_selenium_practice\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/droppable/")
driver.switch_to_frame(0)
sorc=driver.find_element_by_id("draggable")
tgt=driver.find_element_by_id("droppable")

actions = ActionChains(driver)
actions.drag_and_drop(sorc, tgt).perform()