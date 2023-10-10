from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """PageObject класс для главной страницы pochta.ru."""

    def get_auth(self):
        """Переход на страницу авторизации."""
        js_script = (
            "document.querySelector('[href=\"/api/auth/login\"]').click();"
        )
        self.driver.execute_script(js_script)

    def open_search_field(self):
        """Открыть поисковик на сайте."""
        self.find_element(MainPageLocators.OPEN_SEARCH_BUTTON).click()

    def enter_search_query(self, query):
        """Выполнить поиск на сайте."""
        search_field = self.find_element(MainPageLocators.SEARCH_FIELD)
        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.RETURN)

    def get_search_result(self):
        """Получить результаты поиска."""
        return self.find_element(MainPageLocators.SEARCH_RESULT).text

    def menu_item(self):
        """Переход в верхнее меню."""
        menu_item = self.find_element(MainPageLocators.MENU_ITEM)
        ActionChains(self.driver).move_to_element(menu_item).perform()

    def select_posylka_option(self):
        """Переход на страницу Отправить посылку."""
        posylka_option = self.find_element(MainPageLocators.POSYLKA_OPTION)
        self.driver.execute_script("arguments[0].click();", posylka_option)
