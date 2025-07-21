from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

expected_users = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"]
password_users = "secret_sauce"

class LoginBottomPanel(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_credentials = page.locator('[data-test="login-credentials"]')
        self.login_password = page.locator('[data-test="login-password"]')
    def login_bottom(self):
        expect(self.login_credentials).to_be_visible()
        credentials_text = self.login_credentials.inner_text()
        assert "Accepted usernames are:" in credentials_text
        for user in expected_users:
            assert user in credentials_text, f"Username '{user}' not found in login_credentials"

        expect(self.login_password).to_be_visible()
        login_password_text = self.login_password.inner_text()
        assert "Password for all users:" in login_password_text
        assert password_users in login_password_text, f"Password '{password_users}' not found in login_password_text"

