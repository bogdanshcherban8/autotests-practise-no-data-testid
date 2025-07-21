import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.inventory_page.inventory_page import InventoryPage


@pytest.mark.regression
def test_cart(chromium_page:Page, cart_page:CartPage, login_page: LoginPage, inventory_page: InventoryPage):
    cart_page.visit("https://www.saucedemo.com/")
    login_page.login_form("standard_user", 'secret_sauce')
    cart_page.add_check()
    cart_page.cart_badge_page()
    inventory_page.navbar_inventory.navbar_top_check()
    inventory_page.navbar_inventory.navbar_low_check()
    inventory_page.sidebar_inventory.sidebar_check()