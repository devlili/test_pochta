from pages.base_page import BasePage
from pages.locators import SendPackageLocators


class SendPackagePage(BasePage):
    """PageObject класс для страницы 'Оформить посылку'."""

    def get_button_placeholders(self):
        """Получить плейсхолдеры полей."""
        button_placeholder_dict = {}
        buttons = self.find_elements(SendPackageLocators.WHERE_SECTION)

        for button in buttons:
            button_text = button.text
            button.click()
            input_field = self.find_elements(SendPackageLocators.INPUT_FIELD)
            placeholder = input_field[1].get_attribute("placeholder")
            button_placeholder_dict[button_text] = placeholder

        return button_placeholder_dict
