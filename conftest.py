import pytest

# @pytest.fixture(scope="function")
# def browser_context(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }

@pytest.fixture(scope="function")
def browser_context(playwright, browser_context_args):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(viewport=None)  # Ensure maximized window
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page(browser_context, base_url):
    page = browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()
