from playwright.sync_api import sync_playwright

url_login = 'https://the-internet.herokuapp.com/login'

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page()
    page.goto(url_login)
    page.locator('id=username').fill('farid')
    page.locator('text=Elemental Selenium').click()
    page.locator('text=Elemental').click()
    
    h2 = page.locator('h2')
    print(h2.all_text_contents())

    _a = page.locator('a')
    print(_a.count())

    page.pause()
