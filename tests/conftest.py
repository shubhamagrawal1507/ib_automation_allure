import pytest
from playwright.sync_api import Playwright


URL = "https://infobeans.com/"

@pytest.fixture()
def setup(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(url=URL,timeout=60000)
    yield page
    page.close()
    context.close()
    browser.close()
