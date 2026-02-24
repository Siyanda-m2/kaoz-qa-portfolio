import pytest
import allure
from playwright.sync_api import Page
from e2e.pages.login_page import LoginPage

@allure.feature("Authentication")
class TestLogin:

    @allure.story("Valid login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, page: Page):
        with allure.step("Navigate to login page"):
            login = LoginPage(page)
            login.navigate()
        with allure.step("Login with valid credentials"):
            login.login("standard_user", "secret_sauce")
        with allure.step("Verify redirect to inventory"):
            assert page.url == "https://www.saucedemo.com/inventory.html"

    @allure.story("Invalid login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self, page: Page):
        with allure.step("Navigate to login page"):
            login = LoginPage(page)
            login.navigate()
        with allure.step("Login with invalid credentials"):
            login.login("wrong_user", "wrong_pass")
        with allure.step("Verify error message"):
            assert "Epic sadface" in login.get_error_message()

    @allure.story("Empty credentials")
    @allure.severity(allure.severity_level.MINOR)
    def test_empty_credentials(self, page: Page):
        with allure.step("Navigate to login page"):
            login = LoginPage(page)
            login.navigate()
        with allure.step("Submit empty credentials"):
            login.login("", "")
        with allure.step("Verify validation message"):
            assert "Username is required" in login.get_error_message()