from playwright.sync_api import Page, expect

from components.cart.checkout_error import CheckoutError
from components.cart.price import Price
from pages.base_page import BasePage

payment_info_text =['Payment Information:', 'SauceCard #31337']
shipping_info_text =['Shipping Information:', 'Free Pony Express Delivery!']
class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_error = CheckoutError(page)
        self.price = Price(page)
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.checkout_top_information = page.locator('[data-test="secondary-header"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.payment_info= page.locator('[data-test^="payment-info-"]')
        self.shipping_info = page.locator('[data-test^="shipping-info-"]')
        self.total_info = page.locator('[data-test="total-info-label"]')

    def checkout_check(self):
        self.checkout_button.click()
        expect(self.checkout_top_information).to_be_visible()
        expect(self.checkout_top_information).to_contain_text('Checkout: Your Information')
        expect(self.first_name).to_be_visible()
        expect(self.first_name).to_have_attribute("placeholder", "First Name")
        expect(self.last_name).to_be_visible()
        expect(self.last_name).to_have_attribute("placeholder", "Last Name")
        expect(self.postal_code).to_be_visible()
        expect(self.postal_code).to_have_attribute("placeholder", "Zip/Postal Code")
        expect(self.cancel_button).to_be_visible()
        expect(self.continue_button).to_be_visible()

    def enter_data(self, firstname: str, lastname: str, zipcode: str):
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.postal_code.fill(zipcode)
        self.continue_button.click()
    def checkout_overview(self):
        expect(self.checkout_top_information).to_be_visible()
        expect(self.checkout_top_information).to_contain_text('Checkout: Overview')
        for i in range(len(payment_info_text)):
            expect(self.payment_info.nth(i)).to_be_visible()
            expect(self.payment_info.nth(i)).to_contain_text(payment_info_text[i])
        for i in range(len(shipping_info_text)):
            expect(self.shipping_info.nth(i)).to_be_visible()
            expect(self.shipping_info.nth(i)).to_contain_text(shipping_info_text[i])
        expect(self.total_info).to_be_visible()
        expect(self.total_info).to_contain_text('Price Total')

