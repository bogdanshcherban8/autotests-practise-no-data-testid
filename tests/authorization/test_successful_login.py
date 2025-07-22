

import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage

valid_users = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
]
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@allure.severity(Severity.BLOCKER)
@allure.epic(AllureEpic.AUTHORIZATION_SYSTEM)
@allure.feature(AllureFeature.AUTHORIZATION)
@allure.story(AllureStory.LOGIN_FUNCTIONALITY)
@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize("username", valid_users)
@allure.title("User successfully login with 5 logins and 1 password")
def test_successful_login(chromium_page: Page, login_page: LoginPage, username):
    login_page.visit('https://www.saucedemo.com/')
    with allure.step("Login logic checking"):
        login_page.login_bottom_panel.login_bottom()
        login_page.login_form(username, 'secret_sauce')
        login_page.errors_during_login.errors_login_off()
