from playwright.sync_api import sync_playwright
from config.config import BASE_URL,USERNAME,PASSWORD
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()
    input("Press Enter to close browser...")

