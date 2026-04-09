from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page : Page):
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_button = page.locator("#remove-sauce-labs-backpack")


    def add_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.remove_button).to_be_visible()

    def remove_from_cart(self):
        self.remove_button.click()
        expect(self.add_to_cart_button).to_be_visible()