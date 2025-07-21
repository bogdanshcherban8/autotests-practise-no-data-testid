from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarInventory(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.sidebar_items_list = page.locator('[data-test="inventory-sidebar-link"]')
        self.sidebar_about = page.locator('[data-test="about-sidebar-link"]')
        self.sidebar_logout = page.locator('[data-test="logout-sidebar-link"]')
        self.sidebar_reset_app = page.locator('[data-test="reset-sidebar-link"]')
    def sidebar_check(self):
        expect(self.sidebar_items_list).to_be_visible()
        expect(self.sidebar_items_list).to_have_text("All Items")
        expect(self.sidebar_about).to_be_visible()
        expect(self.sidebar_about).to_have_text("About")
        expect(self.sidebar_logout).to_be_visible()
        expect(self.sidebar_logout).to_have_text("Logout")
        expect(self.sidebar_reset_app).to_be_visible()
        expect(self.sidebar_reset_app).to_have_text("Reset App State")


