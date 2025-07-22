import allure
import pytest
from playwright.sync_api import Page

from pages.authorization.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.inventory.inventory_page import InventoryPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@allure.epic(AllureEpic.PRODUCT_DETAILS)
@allure.feature(AllureFeature.CART)
@allure.story(AllureStory.CART_MANAGEMENT)
@pytest.mark.cart
@pytest.mark.regression
@allure.title("Checking the cart operation")
def test_cart(chromium_page: Page, cart_page: CartPage, login_page: LoginPage, inventory_page: InventoryPage):
    cart_page.visit("https://www.saucedemo.com/")
    login_page.login_form("standard_user", 'secret_sauce')
    with allure.step("Interface checking"):
        cart_page.add_check()
        cart_page.cart_badge_page()
        inventory_page.navbar_inventory.navbar_top_check()
        inventory_page.navbar_inventory.navbar_low_check()
        inventory_page.sidebar_inventory.sidebar_check()
