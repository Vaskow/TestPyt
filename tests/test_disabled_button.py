from pages.disabled_button import DisabledButtonPage

def test_select_click(browser):
    disabled_button_page = DisabledButtonPage(browser)
    disabled_button_page.open()
    disabled_button_page.select_list_ctrl_button('enabled')
    disabled_button_page.check_visibility_button()