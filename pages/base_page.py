from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        """
        Ищет и возвращает первый найденный элемент на странице с заданным локатором.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        """
        Ищет и возвращает все найденные элементы на странице с заданным локатором.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    # def is_element_present(self, locator):
    #     """
    #     Проверяет наличие элемента на странице с заданным локатором.
    #     """
    #     try:
    #         self.find_element(locator)
    #     except NoSuchElementException:
    #         return False
    #     return True
