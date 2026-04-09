# login_setup.py
from playwright.sync_api import sync_playwright

STORAGE_FILE = "storage_state.json"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        # Enter credentials directly here
        page.fill('input[data-test="username"]', "standard_user")
        page.fill('input[data-test="password"]', "secret_sauce")
        page.click('input[data-test="login-button"]')

        # Wait for inventory page to load
        page.wait_for_url("https://www.saucedemo.com/inventory.html")

        # Save login state to file
        context.storage_state(path=STORAGE_FILE)
        browser.close()
        print(f"Login session saved to {STORAGE_FILE}")

if __name__ == "__main__":
    main()