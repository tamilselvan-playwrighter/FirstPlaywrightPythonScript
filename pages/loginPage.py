from playwright.sync_api import Page,expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_textfield = page.locator('input[data-test="username"]')
        self.password_textfield = page.locator('input[data-test="password"]')
        self.login_button = page.locator('input[data-test="login-button"]')


    def login_to_application(self, username, password):
        self.username_textfield.fill(username)
        self.password_textfield.fill(password)
        self.login_button.click()
        try:
            self.page.wait_for_url("https://www.saucedemo.com/inventory.html", timeout=5000)
            expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        except Exception as e:
            raise AssertionError(f"Login failed: {e}")




