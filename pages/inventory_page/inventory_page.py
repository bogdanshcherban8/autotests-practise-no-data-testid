from playwright.sync_api import Page, expect

from components.inventory.navbar_inventory import NavbarInventory
from components.inventory.sidebar_inventory import SidebarInventory
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar_inventory = NavbarInventory(page)
        self.sidebar_inventory = SidebarInventory(page)

    def check_items(self):


