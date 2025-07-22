import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CheckoutError(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.error_case = page.locator('[data-test="error"]')
        self.error_button = page.locator('[data-test="error-button"]')
    def error_case_off(self):
        expect(self.error_case).not_to_be_visible()
        self.check_current_url(re.compile(r".*/checkout-step-one"))
    def error_case_on(self, expected_text=str):
        expect(self.error_case).to_be_visible()
        expect(self.error_case).to_have_text(expected_text)
        expect(self.error_button).to_be_visible()
        self.check_current_url(re.compile(r".*/checkout-step-one"))