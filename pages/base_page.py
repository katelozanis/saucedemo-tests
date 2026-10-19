from urllib.parse import urlparse
from playwright.sync_api import Page, Locator, expect


class BasePage:
    """Base page object providing condition-based wait helpers and common actions.

    Follows project standards:
    - Never uses fixed sleeps or pauses.
    - Waits on conditions (visible, clickable, URL changed, text present).
    - Page objects encapsulate all locators; tests call methods and never contain locators.
    """

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def get_url_path(self) -> str:
        parsed = urlparse(self.page.url)
        return parsed.path or "/"

    def wait_for_url_path(self, expected_path: str, timeout: float = 10000) -> None:
        # Condition-based wait: wait until URL path matches expected path
        self.page.wait_for_url(lambda url: urlparse(url).path == expected_path, timeout=timeout)

    def wait_until_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()

    def wait_until_hidden(self, locator: Locator) -> None:
        expect(locator).to_be_hidden()
