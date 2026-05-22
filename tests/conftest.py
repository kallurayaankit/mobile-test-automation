import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def mobile_page():
    """Create a mobile browser context using iPhone 13 emulation."""
    with sync_playwright() as p:
        iphone = p.devices["iPhone 13"]
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**iphone)
        page = context.new_page()
        yield page
        context.close()
        browser.close()