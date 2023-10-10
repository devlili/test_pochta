from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    """PageObject класс для страницы авторизации."""

    def click_login_button(self):
        """Нажать на кнопку Войти."""
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def is_login_button_disabled(self):
        """Проверка активности кнопки Войти."""
        login_button = self.find_element(
            LoginPageLocators.LOGIN_BUTTON_DISABLED
        )
        return login_button is not None

    def is_email_phone_field_empty(self):
        """Проверка пустого поля 'Электронная почта или телефон'."""
        email_phone_field = self.find_element(
            LoginPageLocators.EMAIL_PHONE_FIELD
        )
        return email_phone_field.get_attribute("value") == ""

    def is_password_field_empty(self):
        """Проверка пустого поля 'Пароль'."""
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        return password_field.get_attribute("value") == ""

    def enter_invalid_email_phone(self, value):
        """Ввод недопустимых значений."""
        email_phone_field = self.find_element(
            LoginPageLocators.EMAIL_PHONE_FIELD
        )
        email_phone_field.clear()
        email_phone_field.send_keys(value)

    def get_username_error_message(self):
        """Получить валидационное сообщение."""
        username_error_message = self.find_element(
            LoginPageLocators.EMAIL_PHONE_ERROR_MESSAGE
        ).text
        return username_error_message
