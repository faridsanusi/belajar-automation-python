from selenium import webdriver
from selenium.webdriver.common.by import By


url_login = 'https://the-internet.herokuapp.com/login'

driver = webdriver.Chrome()

driver.get(url_login)
driver.find_element(By.ID, 'username').send_keys('farid')
driver.find_element(By.LINK_TEXT, 'Elemental Selenium').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Elemental').click()

h2 = driver.find_element(By.TAG_NAME , 'h2')
print(h2.text)

h2s = driver.find_elements(By.TAG_NAME , 'h2')
print(h2s)

_a = driver.find_element(By.TAG_NAME , 'a')
print(_a.text)

_as = driver.find_elements(By.TAG_NAME , 'a')
print(len(_as))


