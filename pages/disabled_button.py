from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

list_selector = (By.CSS_SELECTOR, '#id_select_state')
button_selector = (By.CSS_SELECTOR, '#submit-id-submit')

class DisabledButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.qa-practice.com/elements/button/disabled')

    def list_ctrl_button(self):
        return Select(self.find(list_selector))

    def select_list_ctrl_button(self, value_str): #выбрать значение списка
        select = self.list_ctrl_button()
        select.select_by_value(value_str)

    def check_visibility_button(self):
        try:
            self.browser.wait.until(
                EC.visibility_of_element_located(button_selector)
            )
            assert True
        except TimeoutException:
            print('Кнопка не появилась на экране')
            assert False