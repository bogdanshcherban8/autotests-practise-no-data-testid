from playwright.sync_api import Page, expect

from components.inventory.navbar_inventory import NavbarInventory
from components.inventory.product_sort_container import ProductSortContainer
from components.inventory.sidebar_inventory import SidebarInventory
from components.inventory.sidebar_menu import SidebarMenu
from pages.base_page import BasePage

expected_titles = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                   'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
expected_description = [
    'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.',
    "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
    "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
    "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
    "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
    "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."]
expected_price = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar_inventory = NavbarInventory(page)
        self.sidebar_inventory = SidebarInventory(page)
        self.sidebar_menu = SidebarMenu(page)
        self.product_sort_container = ProductSortContainer(page)
        self.item_image = page.locator('[data-test^="inventory-item-"][data-test$="-img"]')
        self.item_title = page.locator('[data-test="inventory-item-name"]')
        self.item_description = page.locator('[data-test="inventory-item-desc"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.item_add_cart = page.locator('[data-test^="add-to-cart-"]')
        self.item_back_button = page.locator('[data-test="back-to-products"]')
    def check_items(self):
        for i in range(len(expected_titles)):
            expect(self.item_title.nth(i)).to_be_visible()
            expect(self.item_title.nth(i)).to_contain_text(expected_titles[i])
        count = self.item_image.count()
        for i in range(count):
            expect(self.item_image.nth(i)).to_be_visible()
        for i in range(len(expected_description)):
            expect(self.item_description.nth(i)).to_be_visible()
            expect(self.item_description.nth(i)).to_contain_text(expected_description[i])
        for i in range(len(expected_price)):
            expect(self.item_price.nth(i)).to_be_visible()
            expect(self.item_price.nth(i)).to_contain_text(expected_price[i])
        cart = self.item_add_cart.count()
        for i in range(cart):
            expect(self.item_add_cart.nth(i)).to_be_visible()
            expect(self.item_add_cart.nth(i)).to_have_text('Add to cart')

    def current_item_check(self):
        for i in range(len(expected_titles)):
            title_on_main = self.item_title.nth(i).inner_text()
            desc_on_main = self.item_description.nth(i).inner_text()
            price_on_main = self.item_price.nth(i).inner_text()

            self.item_title.nth(i).click()

            product_title = self.page.locator('[data-test="inventory-item-name"]').inner_text()
            product_desc = self.page.locator('[data-test="inventory-item-desc"]').inner_text()
            product_price = self.page.locator('[data-test="inventory-item-price"]').inner_text()

            assert product_title == title_on_main, f"Title mismatch: {product_title} != {title_on_main}"
            assert product_desc == desc_on_main, f"Description mismatch: {product_desc} != {desc_on_main}"
            assert product_price == price_on_main, f"Price mismatch: {product_price} != {price_on_main}"

            self.item_back_button.click()

        count = self.item_image.count()
        for i in range(count):
            expect(self.item_image.nth(i)).to_be_visible()

        cart = self.item_add_cart.count()
        for i in range(cart):
            expect(self.item_add_cart.nth(i)).to_be_visible()
            expect(self.item_add_cart.nth(i)).to_have_text('Add to cart')

