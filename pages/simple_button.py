from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

button_selector = (By.CSS_SELECTOR, '#submit-id-submit')
result_selector = (By.CSS_SELECTOR, '#result-text')

class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/simple')

    @property
    def button(self):
        return self.find(button_selector)

    def button_click(self):
        return self.button.click()

    @property
    def button_is_displayed(self):
        return self.button.is_displayed()

    @property
    def result(self):
        return self.find(result_selector)

    def check_result_text(self, text):
        try:
            result = self.browser.wait.until(
                EC.visibility_of_element_located(result_selector)
            )
            assert result.text == text, 'Текст элемента не соответствует заявленному'
        except TimeoutException:
            print('Элемент не появился на экране')
            assert False
