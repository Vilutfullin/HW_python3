import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def browser_size():
    browser.open('https://duckduckgo.com/')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.close()

