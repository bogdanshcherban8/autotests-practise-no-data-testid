import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@allure.severity(Severity.MINOR)
@allure.epic(AllureEpic.PRODUCT_DETAILS)
@allure.feature(AllureFeature.SIDEBAR)
@allure.story(AllureStory.MENU_INTERACTION)
@pytest.mark.regression
@allure.title("Checking the sidebar")
def test_sidebar(chromium_page:Page, inventory_page:InventoryPage, login_page: LoginPage):
    inventory_page.visit('https://www.saucedemo.com/')
    login_page.login_form("standard_user", 'secret_sauce')
    with allure.step("Interface checking"):
        inventory_page.navbar_inventory.navbar_top_check()
        inventory_page.navbar_inventory.navbar_low_check()
        inventory_page.sidebar_inventory.sidebar_check()
        inventory_page.sidebar_menu.menu_check()