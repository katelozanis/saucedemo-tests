import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from config.settings import HEADLESS


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
