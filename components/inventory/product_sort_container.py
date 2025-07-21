from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class ProductSortContainer(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.header_container = page.locator('[data-test="secondary-header"]')
        self.active_option = page.locator('[data-test="active-option"]')
        self.item_titles = page.locator('[data-test="inventory-item-name"]')
        self.item_prices = page.locator('[data-test="inventory-item-price"]')
    def product_check(self, option_text: str):
        expect(self.header_container).to_be_visible()
        expect(self.header_container).to_contain_text('Products')
        self.sort_dropdown.select_option(label=option_text)
        expect(self.active_option).to_contain_text(option_text)

        if option_text in ['Name (A to Z)', 'Name (Z to A)']:
            titles = self.item_titles.all_text_contents()
            sorted_titles = sorted(titles)
            if option_text == 'Name (Z to A)':
                sorted_titles.reverse()
            assert titles == sorted_titles, f"Items not sorted correctly by {option_text}"

        elif option_text in ['Price (low to high)', 'Price (high to low)']:
            prices = [
                float(price.replace('$', ''))
                for price in self.item_prices.all_text_contents()
            ]
            sorted_prices = sorted(prices)
            if option_text == 'Price (high to low)':
                sorted_prices.reverse()
            assert prices == sorted_prices, f"Items not sorted correctly by {option_text}"