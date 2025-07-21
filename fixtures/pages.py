import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage


@pytest.fixture
def login_page(chromium_page: Page)->LoginPage:
    return LoginPage(page=chromium_page)
@pytest.fixture
def inventory_page(chromium_page: Page)->InventoryPage:
    return InventoryPage(page=chromium_page)