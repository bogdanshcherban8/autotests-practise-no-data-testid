from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ErrorsDurinLogin(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.errors_login = page.locator('[data-test="error"]')
        self.errors_button = page.locator('[data-test="error-button"]')

    def errors_login_off(self):
        expect(self.errors_login).not_to_be_visible()

    def errors_login_on(self, expected_text=str):
        expect(self.errors_login).to_be_visible()
        expect(self.errors_login).to_have_text(expected_text)
        expect(self.errors_button).to_be_visible()

