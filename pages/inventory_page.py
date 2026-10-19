from typing import List
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for Sauce Demo Inventory Page (URL path /inventory.html)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_heading = self.page.locator('[data-test="title"]')
        self.inventory_items = self.page.locator('[data-test="inventory-item"]')
        self.item_names = self.page.locator('[data-test="inventory-item-name"]')
        self.item_prices = self.page.locator('[data-test="inventory-item-price"]')
        self.sort_dropdown = self.page.locator('[data-test="product-sort-container"]')
        self.active_sort_option = self.page.locator(".active_option")
        self.cart_badge = self.page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = self.page.locator('[data-test="shopping-cart-link"]')
        self.burger_menu_button = self.page.locator("#react-burger-menu-btn")
        self.logout_link = self.page.locator('[data-test="logout-sidebar-link"]')

    def get_heading_text(self) -> str:
        expect(self.page_heading).to_be_visible()
        return self.page_heading.text_content() or ""

    def get_product_count(self) -> int:
        return self.inventory_items.count()

    def get_product_names(self) -> List[str]:
        return [name.strip() for name in self.item_names.all_text_contents()]

    def get_product_prices_numeric(self) -> List[float]:
        price_texts = self.item_prices.all_text_contents()
        return [float(p.replace("$", "").strip()) for p in price_texts]

    def get_selected_sort_option(self) -> str:
        return (self.active_sort_option.text_content() or "").strip()

    def select_sort_option(self, option_label: str) -> None:
        label_to_value = {
            "Name (A to Z)": "az",
            "Name (Z to A)": "za",
            "Price (low to high)": "lohi",
            "Price (high to low)": "hilo",
        }
        val = label_to_value.get(option_label, option_label)
        self.sort_dropdown.select_option(val)
        # Condition-based wait for the active sort label to update
        expect(self.active_sort_option).to_have_text(option_label)

    def get_first_product_name(self) -> str:
        return (self.item_names.first.text_content() or "").strip()

    def get_first_product_price(self) -> str:
        return (self.item_prices.first.text_content() or "").strip()

    def add_first_product_to_cart(self) -> None:
        first_item = self.inventory_items.first
        first_item.locator('[data-test^="add-to-cart"]').click()

    def has_cart_badge(self) -> bool:
        return self.cart_badge.count() > 0 and self.cart_badge.is_visible()

    def get_cart_badge_text(self) -> str:
        expect(self.cart_badge).to_be_visible()
        return (self.cart_badge.text_content() or "").strip()

    def click_cart(self) -> None:
        self.cart_link.click()

    def open_burger_menu(self) -> None:
        self.burger_menu_button.click()
        expect(self.logout_link).to_be_visible()

    def click_logout(self) -> None:
        self.open_burger_menu()
        self.logout_link.click()
