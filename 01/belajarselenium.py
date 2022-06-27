from selenium import webdriver

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

driver1.get('https://www.google.co.id')
driver2.get('https://www.github.com')
driver3.get('https://www.bing.com')
