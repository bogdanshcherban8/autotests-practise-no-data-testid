import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage

test_cases = [
    ("", "", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("fake_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
]
@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected_error", test_cases)
def test_wrong_login(chromium_page: Page, login_page: LoginPage, username, password, expected_error):
    login_page.visit('https://www.saucedemo.com/')
    login_page.login_bottom_panel.login_bottom()
    login_page.login_form(username, password)
    login_page.errors_during_login.errors_login_on(expected_error)
