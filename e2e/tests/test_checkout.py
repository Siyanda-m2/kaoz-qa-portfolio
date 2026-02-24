import pytest
from playwright.sync_api import Page
from e2e.pages.login_page import LoginPage
from e2e.pages.inventory_page import InventoryPage
from e2e.pages.cart_page import CartPage
from e2e.pages.checkout_page import CheckoutPage

class TestCheckout:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        self.inventory = InventoryPage(page)
        self.cart = CartPage(page)
        self.checkout = CheckoutPage(page)

    def test_full_checkout_flow(self, page: Page):
        self.inventory.add_product_to_cart(0)
        self.inventory.go_to_cart()
        assert self.cart.get_cart_item_count() == 1
        self.cart.proceed_to_checkout()
        self.checkout.fill_details("Kaoz", "Dev", "1337")
        self.checkout.continue_checkout()
        self.checkout.finish_order()
        assert "Thank you" in self.checkout.get_confirmation_text()

    def test_checkout_requires_first_name(self, page: Page):
        self.inventory.add_product_to_cart(0)
        self.inventory.go_to_cart()
        self.cart.proceed_to_checkout()
        self.checkout.fill_details("", "Dev", "1337")
        self.checkout.continue_checkout()
        assert "First Name is required" in self.checkout.get_error_message()

    def test_checkout_requires_last_name(self, page: Page):
        self.inventory.add_product_to_cart(0)
        self.inventory.go_to_cart()
        self.cart.proceed_to_checkout()
        self.checkout.fill_details("Kaoz", "", "1337")
        self.checkout.continue_checkout()
        assert "Last Name is required" in self.checkout.get_error_message()

    def test_checkout_requires_postal_code(self, page: Page):
        self.inventory.add_product_to_cart(0)
        self.inventory.go_to_cart()
        self.cart.proceed_to_checkout()
        self.checkout.fill_details("Kaoz", "Dev", "")
        self.checkout.continue_checkout()
        assert "Postal Code is required" in self.checkout.get_error_message()

    def test_cart_retains_correct_item(self, page: Page):
        names = self.inventory.get_product_names()
        first_product = names[0]
        self.inventory.add_product_to_cart(0)
        self.inventory.go_to_cart()
        cart_names = self.cart.get_cart_item_names()
        assert first_product in cart_names