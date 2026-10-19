from playwright.sync_api import Page, expect
from config.settings import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for Sauce Demo Login Page (URL path /)."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = self.page.locator('[data-test="username"]')
        self.password_input = self.page.locator('[data-test="password"]')
        self.login_button = self.page.locator('[data-test="login-button"]')
        self.error_container = self.page.locator('[data-test="error"]')

    def open(self) -> "LoginPage":
        self.navigate(BASE_URL)
        return self

    def enter_username(self, username: str) -> None:
        self.username_input.fill(username)

    def enter_password(self, password: str) -> None:
        self.password_input.fill(password)

    def click_login(self) -> None:
        self.login_button.click()

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_button_visible(self) -> bool:
        return self.login_button.is_visible()

    def wait_for_login_button(self) -> None:
        expect(self.login_button).to_be_visible()

    def is_error_visible(self) -> bool:
        return self.error_container.is_visible()

    def get_error_text(self) -> str:
        expect(self.error_container).to_be_visible()
        return self.error_container.text_content() or ""
