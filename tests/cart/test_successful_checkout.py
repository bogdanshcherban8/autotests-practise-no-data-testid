import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from fixtures.pages import checkout_page
from pages.authorization.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.cart.checkout_page import CheckoutPage
from pages.inventory.inventory_page import InventoryPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
@allure.severity(Severity.NORMAL)
@allure.epic(AllureEpic.PRODUCT_DETAILS)
@allure.feature(AllureFeature.CHECKOUT)
@allure.story(AllureStory.ORDER_COMPLETION)
@pytest.mark.cart
@pytest.mark.regression
@allure.title("User successfully made an order")
def test_successful_checkout(chromium_page: Page, cart_page: CartPage, login_page: LoginPage, inventory_page: InventoryPage,
                  checkout_page: CheckoutPage):
    checkout_page.visit("https://www.saucedemo.com/")
    login_page.login_form("standard_user", 'secret_sauce')
    with allure.step("Interface checking"):
        cart_page.add_check()
        cart_page.cart_badge_page()
        checkout_page.checkout_check()
        checkout_page.checkout_error.error_case_off()
    with allure.step("Checkout logic check"):
        checkout_page.enter_data("Bob", "pass", "160")
        checkout_page.checkout_overview()
        checkout_page.price.price_details()
