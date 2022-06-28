from playwright.sync_api import sync_playwright
import time

url = 'https://the-internet.herokuapp.com/windows'
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    time.sleep(1)
    context.pages[0].bring_to_front()
    page.wait_for_selector('text=Click Here').click()

    time.sleep(1)
    context.pages[0].bring_to_front()
    page.wait_for_selector('text=Click Here').click()

    time.sleep(1)
    context.pages[0].bring_to_front()
    page.wait_for_selector('text=Click Here').click()

    time.sleep(1)
    context.pages[0].bring_to_front()
    page.wait_for_selector('text=Click Here').click()

    context.pages[0].bring_to_front()
    page.pause()
    # driver.switch_to.window(driver.window_handles[0])

