import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.cart.checkout_page import CheckoutPage
from pages.inventory.inventory_page import InventoryPage


@pytest.fixture
def login_page(chromium_page: Page)->LoginPage:
    return LoginPage(page=chromium_page)
@pytest.fixture
def inventory_page(chromium_page: Page)->InventoryPage:
    return InventoryPage(page=chromium_page)
@pytest.fixture
def cart_page(chromium_page: Page)->CartPage:
    return CartPage(page=chromium_page)
@pytest.fixture
def checkout_page(chromium_page: Page)->CheckoutPage:
    return CheckoutPage(page=chromium_page)
