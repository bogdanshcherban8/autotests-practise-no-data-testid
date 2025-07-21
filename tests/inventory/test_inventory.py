import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage

@pytest.mark.regression
def test_inventory(chromium_page:Page, inventory_page:InventoryPage, login_page: LoginPage):
    inventory_page.visit('https://www.saucedemo.com/')
    login_page.login_form("standard_user", 'secret_sauce')
    inventory_page.navbar_inventory.navbar_top_check()
    inventory_page.navbar_inventory.navbar_middle_check()
    inventory_page.navbar_inventory.navbar_low_check()
    inventory_page.sidebar_inventory.sidebar_check()
    inventory_page.check_items()