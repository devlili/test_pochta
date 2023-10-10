from pages.login_page import LoginPage
from pages.main_page import MainPage

LINK = "https://www.pochta.ru/"


def test_open_login(driver):
    """Проверка перехода на страницу авторизации."""
    main_page = MainPage(driver)
    main_page.open_url(LINK)
    main_page.get_auth()


def test_click_login_button(driver):
    """Проверка отсутствия входа при пустых значениях."""
    login_page = LoginPage(driver)
    login_page.click_login_button()
    assert (
        login_page.is_email_phone_field_empty()
    ), "Поле «Электронная почта или телефон» не пустое."
    assert login_page.is_password_field_empty(), "Поле «Пароль» не пустое."
    assert (
        login_page.is_login_button_disabled()
    ), "Кнопка должна быть неактивна."


def test_invalid_input_validation_messages(driver):
    """Негативный тест на валидационные сообщения при авторизации."""
    login_page = LoginPage(driver)
    login_page.enter_invalid_email_phone("     ")
    validation_message1 = login_page.get_username_error_message()
    print(f"Валидационное сообщение для пробелов: {validation_message1}")

    login_page.enter_invalid_email_phone("123")
    validation_message2 = login_page.get_username_error_message()
    print(
        "Валидационное сообщение для некорректного номера телефона:"
        f" {validation_message2}"
    )
