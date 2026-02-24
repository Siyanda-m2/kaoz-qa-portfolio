from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping = page.locator("[data-test='continue-shopping']")

    def get_cart_item_count(self):
        return self.cart_items.count()

    def get_cart_item_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def proceed_to_checkout(self):
        self.checkout_button.click()