import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
test_cases = ['Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)']
@pytest.mark.regression
@pytest.mark.parametrize('tests', test_cases)
def test_inventory(chromium_page:Page, inventory_page:InventoryPage, login_page: LoginPage, tests):
    inventory_page.visit('https://www.saucedemo.com/')
    login_page.login_form("standard_user", 'secret_sauce')
    inventory_page.navbar_inventory.navbar_top_check()
    inventory_page.navbar_inventory.navbar_low_check()
    inventory_page.sidebar_inventory.sidebar_check()
    inventory_page.check_items()
    inventory_page.current_item_check()
    inventory_page.product_sort_container.product_check(tests)