import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    """Фикстура для создания экземпляра WebDriver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
