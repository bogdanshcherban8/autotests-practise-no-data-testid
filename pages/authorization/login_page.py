from playwright.sync_api import Page, expect

from components.authorization.errors_during_login import ErrorsDurinLogin
from components.authorization.login_bottom_panel import LoginBottomPanel
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_bottom_panel = LoginBottomPanel(page)
        self.errors_during_login = ErrorsDurinLogin(page)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
    def login_form(self, username: str, password: str):
        expect(self.username_input).to_be_visible()
        self.username_input.fill(username)
        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
        expect(self.login_button).to_be_visible()
        self.login_button.click()
