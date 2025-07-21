import os

import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage

valid_users = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
]
@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize("username", valid_users)
def test_successful_login(chromium_page: Page, login_page: LoginPage, username):
    login_page.visit('https://www.saucedemo.com/')
    login_page.login_bottom_panel.login_bottom()
    login_page.login_form(username, 'secret_sauce')
    login_page.errors_during_login.errors_login_off()
