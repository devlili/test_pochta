from pages.search_page import SearchResultsPage


def test_search_for_pochta_rus(driver):
    """Вывод количества найденных результатов по поиску «Почта РФ» в google."""
    search_page = SearchResultsPage(driver)
    search_page.open_url("https://google.ru")
    search_page.search_for_query("Почта РФ")
    results_count = search_page.get_search_results_count()
    print(results_count)


def test_get_search_results(driver):
    """Проверка перехода по ссылке из результата поиска на pochta.ru."""
    search_page = SearchResultsPage(driver)
    search_page.click_pochta_link()
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to.window(windows[0])
        driver.close()
        driver.switch_to.window(windows[-1])
    assert (
        "https://www.pochta.ru" in driver.current_url
    ), "Нет перехода на страницу pochta.ru"
