from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for Sauce Demo Checkout Pages."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = self.page.locator('[data-test="firstName"]')
        self.last_name_input = self.page.locator('[data-test="lastName"]')
        self.postal_code_input = self.page.locator('[data-test="postalCode"]')
        self.continue_button = self.page.locator('[data-test="continue"]')
        self.cancel_button = self.page.locator('[data-test="cancel"]')
        self.finish_button = self.page.locator('[data-test="finish"]')
        self.error_container = self.page.locator('[data-test="error"]')
        self.complete_header = self.page.locator('[data-test="complete-header"]')

    def enter_first_name(self, first_name: str) -> None:
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.last_name_input.fill(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        self.postal_code_input.fill(postal_code)

    def fill_information(self, first_name: str = "", last_name: str = "", postal_code: str = "") -> None:
        if first_name:
            self.enter_first_name(first_name)
        if last_name:
            self.enter_last_name(last_name)
        if postal_code:
            self.enter_postal_code(postal_code)

    def click_continue(self) -> None:
        self.continue_button.click()

    def click_finish(self) -> None:
        self.finish_button.click()

    def is_error_visible(self) -> bool:
        return self.error_container.is_visible()

    def get_error_text(self) -> str:
        expect(self.error_container).to_be_visible()
        return self.error_container.text_content() or ""

    def get_complete_header_text(self) -> str:
        expect(self.complete_header).to_be_visible()
        return self.complete_header.text_content() or ""
