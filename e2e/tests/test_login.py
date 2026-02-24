import pytest
from playwright.sync_api import Page
from e2e.pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")
        assert page.url == "https://www.saucedemo.com/inventory.html"

    def test_invalid_login(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("wrong_user", "wrong_pass")
        assert "Epic sadface" in login.get_error_message()

    def test_empty_credentials(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login("", "")
        assert "Username is required" in login.get_error_message()