import re

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

complete_text = ['Thank you for your order!',
                 'Your order has been dispatched, and will arrive just as fast as the pony can get there!']


class Price(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.item_total_text = page.locator('[data-test="subtotal-label"]')
        self.tax_text = page.locator('[data-test="tax-label"]')
        self.total_text = page.locator('[data-test="total-label"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_panel = page.locator('[data-test="secondary-header"]')
        self.image = page.locator('[data-test="pony-express"]')
        self.header = page.locator('[data-test^="complete-"]')
        self.home_button = page.locator('[data-test="back-to-products"]')
        self.item_prices = page.locator('[data-test="inventory-item-price"]')

    def price_details(self):
        prices_text = self.item_prices.all_inner_texts()
        item_sum = sum(float(price.replace('$', '').strip()) for price in prices_text)

        site_item_total = float(self.item_total_text.inner_text().split('$')[1].strip())
        site_tax = float(self.tax_text.inner_text().split('$')[1].strip())
        site_total = float(self.total_text.inner_text().split('$')[1].strip())

        calculated_total = round(site_item_total + site_tax, 2)

        assert round(item_sum, 2) == round(site_item_total, 2), \
            f"Item total mismatch: calculated {item_sum}, site {site_item_total}"
        assert round(calculated_total, 2) == round(site_total, 2), \
            f"Total mismatch: calculated {calculated_total}, site {site_total}"

        print(f"✔ Subtotal, tax, and total match site values.")
        expect(self.finish_button).to_be_visible()
        self.finish_button.click()
        expect(self.complete_panel).to_be_visible()
        expect(self.complete_panel).to_contain_text("Checkout: Complete!")
        expect(self.image).to_be_visible()
        for i in range(len(complete_text)):
            expect(self.header.nth(i)).to_be_visible()
            expect(self.header.nth(i)).to_contain_text(complete_text[i])
        expect(self.home_button).to_be_visible()
        self.check_current_url(re.compile(r".*/checkout-complete"))
        self.home_button.click()
        self.check_current_url(re.compile(r".*/inventory"))