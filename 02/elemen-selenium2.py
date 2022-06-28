from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url_login = 'https://the-internet.herokuapp.com/login'

driver = webdriver.Chrome()

driver.get(url_login)
time.sleep(2)
# by class name
driver.find_element(By.CLASS_NAME, 'radius').click()
# by css -> tag button and class 
driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
# by css -> id form and tag button 
driver.find_element(By.CSS_SELECTOR, '#login > button').click()
