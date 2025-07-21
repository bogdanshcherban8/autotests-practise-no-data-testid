

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
cart_list_text=['QTY', "Description"]
class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.item_add = page.locator('[data-test^="add-to-cart-"]')
        self.item_remove = page.locator('[data-test^="remove-"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.top_panel = page.locator('[data-test="secondary-header"]')
        self.cart_list = page.locator('[data-test="cart-list"]')
        self.remove_item = page.locator('[data-test^="remove-"]')
        self.continue_button = page.locator('[data-test="continue-shopping"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
    def add_check(self):
        total_items = self.item_add.count()
        for i in range(total_items):
            add_button = self.item_add.first
            expect(add_button).to_be_visible()
            add_button.click()
            remove_button = self.item_remove.first
            expect(remove_button).to_be_visible()

        expect(self.cart_badge).to_be_visible()
        expect(self.cart_badge).to_contain_text(str(total_items))
    def cart_badge_page(self):
        self.cart_badge.click()
        expect(self.top_panel).to_be_visible()
        expect(self.top_panel).to_have_text("Your Cart")
        expect(self.cart_list).to_be_visible()
        for expected_text in cart_list_text:
            expect(self.cart_list).to_contain_text(expected_text)
        removed_items = self.remove_item.count()
        for i in range(removed_items):
            expect(self.remove_item.nth(i)).to_be_visible()
        expect(self.continue_button).to_be_visible()
        expect(self.checkout_button).to_be_visible()