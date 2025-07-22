import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarMenu(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logout = page.locator('[data-test="logout-sidebar-link"]')
        self.reset = page.locator('[data-test="reset-sidebar-link"]')
        self.item = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart = page.locator('[data-test="shopping-cart-badge"]')

    def menu_check(self):
        self.item.click()
        expect(self.cart).to_contain_text('1')
        self.reset.click()
        expect(self.cart).not_to_be_visible()
        self.logout.click()
        self.check_current_url(re.compile(r".*/"))