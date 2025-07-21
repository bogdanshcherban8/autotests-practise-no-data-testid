from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
expected_social= ['Twitter', 'Facebook', 'LinkedIn']

class NavbarInventory(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_container = page.locator('[data-test="header-container"]')
        self.header_menu_button = page.locator('#react-burger-menu-btn')
        self.header_shopping_link = page.locator('[data-test="shopping-cart-link"]')
        self.low_footer_copy = page.locator('[data-test="footer-copy"]')
        self.low_social = page.locator('[data-test^="social-"]')

    def navbar_top_check(self):
        expect(self.header_container).to_be_visible()
        expect(self.header_container).to_contain_text('Swag Labs')
        expect(self.header_shopping_link).to_be_visible()
        expect(self.header_menu_button).to_be_visible()
        self.header_menu_button.click()
    def navbar_low_check(self):
        expect(self.low_footer_copy).to_be_visible()
        expect(self.low_footer_copy).to_have_text('© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')
        for i in range(len(expected_social)):
            expect(self.low_social.nth(i)).to_be_visible()
            expect(self.low_social.nth(i)).to_contain_text(expected_social[i])