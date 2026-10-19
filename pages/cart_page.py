from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for Sauce Demo Cart Page (URL path /cart.html)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_list = self.page.locator(".cart_list")
        self.cart_items = self.page.locator('[data-test="inventory-item"]')
        self.item_name = self.page.locator('[data-test="inventory-item-name"]')
        self.item_price = self.page.locator('[data-test="inventory-item-price"]')
        self.item_quantity = self.page.locator('[data-test="item-quantity"]')
        self.checkout_button = self.page.locator('[data-test="checkout"]')
        self.continue_shopping_button = self.page.locator('[data-test="continue-shopping"]')

    def wait_for_cart_loaded(self) -> None:
        expect(self.cart_list).to_be_visible()

    def get_items_count(self) -> int:
        self.wait_for_cart_loaded()
        if self.page.locator('[data-test="shopping-cart-badge"]').is_visible():
            # Condition-based wait for the added cart item to render
            self.cart_items.first.wait_for(state="visible")
        return self.cart_items.count()

    def get_first_item_name(self) -> str:
        first_item = self.cart_items.first
        expect(first_item.locator('[data-test="inventory-item-name"]')).to_be_visible()
        return (first_item.locator('[data-test="inventory-item-name"]').text_content() or "").strip()

    def get_first_item_price(self) -> str:
        first_item = self.cart_items.first
        expect(first_item.locator('[data-test="inventory-item-price"]')).to_be_visible()
        return (first_item.locator('[data-test="inventory-item-price"]').text_content() or "").strip()

    def get_first_item_quantity(self) -> int:
        first_item = self.cart_items.first
        expect(first_item.locator('[data-test="item-quantity"]')).to_be_visible()
        raw_qty = (first_item.locator('[data-test="item-quantity"]').text_content() or "").strip()
        return int(raw_qty)

    def click_checkout(self) -> None:
        self.checkout_button.click()

    def remove_first_item(self) -> None:
        first_item = self.cart_items.first
        first_item.locator('[data-test^="remove"]').click()
