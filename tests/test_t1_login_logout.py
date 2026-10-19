from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_T1_login_and_logout(page: Page) -> None:
    """T1: Starter test opening the login page and asserting it."""
    login_page = LoginPage(page)
    login_page.open()

    assert login_page.get_url_path() == "/"
    assert login_page.is_login_button_visible() is True
