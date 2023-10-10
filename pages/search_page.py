import re

from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators import SearchResultsLocators


class SearchResultsPage(BasePage):
    """PageObject класс для поисковой системы."""

    def search_for_query(self, query):
        """Выполнить поиск на сайте."""
        search_field = self.find_element(SearchResultsLocators.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def get_search_results_count(self):
        """Получить количество результатов поиска."""
        search_result_text = self.find_element(
            SearchResultsLocators.SEARCH_RESULT_TEXT
        ).text
        match = re.search(r"(\d{1,3}(?:\s?\d{3})+)", search_result_text)
        if match:
            results_count = match.group(1).replace(" ", ",")
            return f"Количество найденных результатов: {results_count}"
        else:
            return "Результатов нет"

    def click_pochta_link(self):
        """Открыть страницу pochta.ru из поисковика."""
        self.find_element(SearchResultsLocators.POCHTA_LINK).click()
