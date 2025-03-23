from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.wait = WebDriverWait(browser, 10)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()