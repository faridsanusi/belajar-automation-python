from playwright.sync_api import sync_playwright

url_login = 'https://the-internet.herokuapp.com/login'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto(url_login)
    # by css with class name
    page.wait_for_selector('.radius').click()
    # by css -> tag button and class 
    page.wait_for_selector('button.radius').click()
    # by css -> id form and tag button
    page.wait_for_selector('#login > button').click()


    page.pause()
