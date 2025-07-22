from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

expected_list =['All Items', 'About', 'Logout', 'Reset App State']
class SidebarInventory(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.sidebar_list = page.locator('[data-test$="-sidebar-link"]')
    def sidebar_check(self):
        for i in range(len(expected_list)):
            expect(self.sidebar_list.nth(i)).to_be_visible()
            expect(self.sidebar_list.nth(i)).to_contain_text(expected_list[i])




