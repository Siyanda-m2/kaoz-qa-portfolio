import pytest
from playwright.sync_api import Page
from e2e.pages.login_page import LoginPage
from e2e.pages.inventory_page import InventoryPage

class TestInventory:

    @pytest.fixture(autouse=True)
    def login(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        self.inventory = InventoryPage(page)

    def test_inventory_loads_six_products(self, page: Page):
        assert self.inventory.get_product_count() == 6

    def test_products_sort_by_price_low_to_high(self, page: Page):
        self.inventory.sort_by("lohi")
        prices = self.inventory.get_product_prices()
        assert prices == sorted(prices)

    def test_products_sort_by_price_high_to_low(self, page: Page):
        self.inventory.sort_by("hilo")
        prices = self.inventory.get_product_prices()
        assert prices == sorted(prices, reverse=True)

    def test_products_sort_by_name_a_to_z(self, page: Page):
        self.inventory.sort_by("az")
        names = self.inventory.get_product_names()
        assert names == sorted(names)

    def test_add_to_cart_updates_badge(self, page: Page):
        self.inventory.add_product_to_cart(0)
        assert self.inventory.get_cart_count() == 1

    def test_add_multiple_items_to_cart(self, page: Page):
        self.inventory.add_product_to_cart(0)
        self.inventory.add_product_to_cart(1)
        assert self.inventory.get_cart_count() == 2