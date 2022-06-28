from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url_login = 'https://the-internet.herokuapp.com/login'
url_add_remove_element = 'https://the-internet.herokuapp.com/add_remove_elements/'

driver = webdriver.Chrome()

driver.get(url_login)
time.sleep(1)
# by class name
driver.find_element(By.CLASS_NAME, 'radius').click()
# by css -> tag button and class 
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
# by css -> id form and tag button 
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#login > button').click()

time.sleep(1)
driver.get(url_add_remove_element)
driver.find_element(By.CSS_SELECTOR, '#content > div > button').click()

