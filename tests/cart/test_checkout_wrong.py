import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from fixtures.pages import checkout_page
from pages.authorization.login_page import LoginPage
from pages.cart.cart_page import CartPage
from pages.cart.checkout_page import CheckoutPage
from pages.inventory.inventory_page import InventoryPage

test_cases = [("", "", "", "Error: First Name is required"), ("Bob", "", "", "Error: Last Name is required"),
              ("Bob", "pass", "", "Error: Postal Code is required")]
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

@allure.severity(Severity.NORMAL)
@allure.epic(AllureEpic.ERROR_HANDLING)
@allure.feature(AllureFeature.CHECKOUT)
@allure.story(AllureStory.CHECKOUT_ERRORS)
@pytest.mark.cart
@pytest.mark.regression
@pytest.mark.parametrize('firstname, lastname, zipcode, error_message', test_cases)
@allure.title("User filled in the sending data incorrectly")
def test_checkout_wrong(chromium_page: Page, cart_page: CartPage, login_page: LoginPage, inventory_page: InventoryPage,
                        checkout_page: CheckoutPage, firstname, lastname, zipcode, error_message):
    checkout_page.visit("https://www.saucedemo.com/")
    login_page.login_form("standard_user", 'secret_sauce')
    with allure.step("Wrong checkout logic check"):
        cart_page.add_check()
        cart_page.cart_badge_page()
        checkout_page.checkout_check()
        checkout_page.enter_data(firstname, lastname, zipcode)
        checkout_page.checkout_error.error_case_on(error_message)
