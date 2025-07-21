from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class NavbarInventory(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_container = page.locator('[data-test="header-container"]')
        self.header_menu_button = page.locator('#react-burger-menu-btn')
        self.header_shopping_link = page.locator('[data-test="shopping-cart-link"]')
        self.header_product_container = page.locator('[data-test="product-sort-container"]')
        self.low_footer_copy = page.locator('[data-test="footer-copy"]')
        self.low_twitter = page.locator('[data-test="social-twitter"]')
        self.low_facebook = page.locator('[data-test="social-facebook"]')
        self.low_linkedin = page.locator('[data-test="social-linkedin"]')
    def navbar_top_check(self):
        expect(self.header_container).to_be_visible()
        expect(self.header_container).to_contain_text('Swag Labs')
        expect(self.header_shopping_link).to_be_visible()
        expect(self.header_menu_button).to_be_visible()
        self.header_menu_button.click()
    def navbar_middle_check(self):
        expect(self.header_container).to_contain_text('Products')
        expect(self.header_product_container).to_be_visible()
    def navbar_low_check(self):
        expect(self.low_footer_copy).to_be_visible()
        expect(self.low_footer_copy).to_have_text('© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy')
        expect(self.low_twitter).to_be_visible()
        expect(self.low_twitter).to_have_text('Twitter')
        expect(self.low_facebook).to_be_visible()
        expect(self.low_facebook).to_have_text('Facebook')
        expect(self.low_linkedin).to_be_visible()
        expect(self.low_linkedin).to_have_text('LinkedIn')