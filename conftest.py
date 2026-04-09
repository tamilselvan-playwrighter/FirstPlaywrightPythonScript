# conftest.py
import os
import pytest
from playwright.sync_api import sync_playwright
import datetime

STORAGE_FILE = os.path.join(os.path.dirname(__file__), "storage_state.json")


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(viewport=None)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context
        context.tracing.stop(path="reports/trace.zip")  # Save trace file
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    # Perform login steps
    page.goto("https://www.saucedemo.com/")
    page.fill('input[data-test="username"]', "standard_user")
    page.fill('input[data-test="password"]', "secret_sauce")
    page.click('input[data-test="login-button"]')
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    yield page
    page.close()

def pytest_runtest_makereport(item, call):
    # Only act after test call phase
    if call.when == "call":
        outcome = call.excinfo
        if outcome is not None:
            # Test failed
            page = item.funcargs.get("page")
            if page:
                # Unique filename with test name and timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name.replace("/", "_")
                screenshot_path = f"reports/screenshots/{test_name}_{timestamp}_fail.png"
                try:
                    page.screenshot(path=screenshot_path)
                    print(f"Screenshot saved on failure: {screenshot_path}")
                except Exception as e:
                    print(f"Failed to capture screenshot on failure: {e}")
