import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page

