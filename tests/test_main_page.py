import time

from pages.main_page import MainPage

LINK = "https://www.pochta.ru/"


def test_site_search(driver):
    """Проверка поиска по сайту."""
    main_page = MainPage(driver)
    main_page.open_url(LINK)
    search_query = "Совкомбанк"
    main_page.open_search_field()
    main_page.enter_search_query(search_query)
    search_result = main_page.get_search_result()
    assert search_query in search_result, (
        f"Значение в поле поиска '{search_query}' не совпадает с"
        f" информационным блоком: {search_result}"
    )


def test_send_package(driver):
    """Проверка перехода на страницу Отправить посылку."""
    main_page = MainPage(driver)
    main_page.open_url(LINK)
    main_page.menu_item()
    main_page.select_posylka_option()
    time.sleep(3)
