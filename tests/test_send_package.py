from pages.send_package_page import SendPackagePage


def test_get_package_fields_placeholders(driver):
    """Вывод значений плейсхолдера поля под кнопками в разделе «Куда»
    на странице Оформить посылку.
    """
    send_package_page = SendPackagePage(driver)
    send_package_page.open_url("https://www.pochta.ru/parcels")
    placeholders = send_package_page.get_button_placeholders()
    print(placeholders)
