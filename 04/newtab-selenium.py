from selenium import webdriver
from selenium.webdriver.common.by import By

import time

url = 'https://the-internet.herokuapp.com/windows'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
driver.switch_to.window(driver.window_handles[0])

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
driver.switch_to.window(driver.window_handles[0])

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
driver.switch_to.window(driver.window_handles[0])

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
driver.switch_to.window(driver.window_handles[0])

time.sleep(1)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
driver.switch_to.window(driver.window_handles[0])
