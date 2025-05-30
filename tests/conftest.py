import pytest
import logging
from playwright.sync_api import Playwright
import allure
from allure_commons.types import AttachmentType

URL = "https://infobeans.com/"

# Set up logging configuration in conftest.py
def pytest_configure(config):
    # Set up a logger for the whole test suite
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

@pytest.fixture()
def setup(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url=URL,timeout=60000)
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook is called before and after the test function is run
    # 'call' contains information about the test execution (setup, call, teardown)
    outcome = yield  # Run the test function
    report = outcome.get_result()

    # We only care about the 'call' phase (where the test function itself is run)
    # and if the test has failed or broken.
    if report.when == "call" and report.failed:
        # Check if 'page' fixture is available (Playwright's Page object)
        if "setup" in item.fixturenames:
            try:
                page = item.funcargs["setup"]
                # Take screenshot
                screenshot_bytes = page.screenshot(full_page=True) # Full page screenshot
                allure.attach(
                    screenshot_bytes,
                    name=f"Screenshot of {item.name}", # Name based on test name
                    attachment_type=AttachmentType.PNG
                )
                print(f"\n--- Attached screenshot for failed test: {item.name} ---")
            except Exception as e:
                print(f"\n--- Failed to take screenshot for {item.name}: {e} ---")



