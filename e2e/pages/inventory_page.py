from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.product_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_product_count(self):
        return self.product_items.count()

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def add_product_to_cart(self, index: int = 0):
        buttons = self.page.locator(".btn_inventory")
        buttons.nth(index).click()

    def get_cart_count(self):
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content())
        return 0

    def go_to_cart(self):
        self.cart_icon.click()