from selenium.webdriver.common.by import By
from pages.simple_button import SimpleButtonPage

def test_simple_button_exist(browser):
    simple_button_page = SimpleButtonPage(browser)
    simple_button_page.open()
    assert simple_button_page.button_is_displayed

def test_simple_button_click(browser):
    simple_button_page = SimpleButtonPage(browser)
    simple_button_page.open()
    simple_button_page.button_click()
    simple_button_page.check_result_text('Submitted')