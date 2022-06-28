from playwright.sync_api import sync_playwright
import time

url_login = 'https://the-internet.herokuapp.com/login'
url_add_remove_element = 'https://the-internet.herokuapp.com/add_remove_elements/'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto(url_login)
    # by css with class name
    page.wait_for_selector('.radius').click()
    # by css -> tag button and class 
    time.sleep(1)
    page.wait_for_selector('button.radius').click()
    # by css -> id form and tag button
    time.sleep(1)
    page.wait_for_selector('#login > button').click()

    # open new page
    page = browser.new_page()
    page.goto(url_add_remove_element)
    # click by css selector
    page.wait_for_selector('#content > div > button').click()
    page.wait_for_selector('//*[@id="content"]/div/button').click()

    page.pause()
