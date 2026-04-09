from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_textfield = page.locator('input[data-test="username"]')
        self.password_textfield = page.locator('input[data-test="password"]')
        self.login_button = page.locator('input[data-test="login-button"]')
        self.inventory_url = "https://www.saucedemo.com/inventory.html"

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login_to_application(self, username, password):
        self.username_textfield.fill(username)
        self.password_textfield.fill(password)
        self.login_button.click()

        # Validate login success
        self.page.wait_for_url(self.inventory_url, timeout=5000)
        expect(self.page).to_have_url(self.inventory_url)