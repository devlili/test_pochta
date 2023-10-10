import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    """Фикстура для создания экземпляра WebDriver."""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # prefs = {
    #     "download.default_directory": f"{os.getcwd()}/downloads",
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True,
    # }
    # chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
