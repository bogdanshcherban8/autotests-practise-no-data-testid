import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

test_cases = ['Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)']
@allure.severity(Severity.NORMAL)
@allure.epic(AllureEpic.PRODUCT_DETAILS)
@allure.feature(AllureFeature.INVENTORY)
@allure.story(AllureStory.INVENTORY_DISPLAY)
@pytest.mark.regression
@pytest.mark.parametrize('tests', test_cases)
@allure.title("Checking the main page of the site")
def test_inventory(chromium_page:Page, inventory_page:InventoryPage, login_page: LoginPage, tests):
    inventory_page.visit('https://www.saucedemo.com/')
    login_page.login_form("standard_user", 'secret_sauce')
    with allure.step("Interface checking"):
        inventory_page.navbar_inventory.navbar_top_check()
        inventory_page.navbar_inventory.navbar_low_check()
        inventory_page.sidebar_inventory.sidebar_check()
        inventory_page.check_items()
        inventory_page.current_item_check()
        inventory_page.product_sort_container.product_check(tests)