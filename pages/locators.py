from selenium.webdriver.common.by import By


class SearchResultsLocators:
    SEARCH_FIELD = (By.XPATH, "//textarea[@id='APjFqb']")
    SEARCH_RESULT_TEXT = (By.XPATH, "//div[@id='result-stats']")
    POCHTA_LINK = (By.PARTIAL_LINK_TEXT, "https://www.pochta.ru")


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Войти']")
    EMAIL_PHONE_FIELD = (By.XPATH, "//input[@id='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='userpassword']")
    EMAIL_PHONE_ERROR_MESSAGE = (
        By.XPATH,
        (
            "//span[@class='FormCaption-sc-138okmx-0 FormError-sc-8wpn30-0"
            " sc-qRumB cHGndD dsGqzS kATeCm']"
        ),
    )


class MainPageLocators:
    OPEN_SEARCH_BUTTON = (By.CSS_SELECTOR, "svg.Icon-sc-jviuxr-0.fbpCIU")
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Поиск по сайту']")
    SEARCH_RESULT = (By.XPATH, "//span[@class='Font-sc-le1wax-0 hftVBh']")
    MENU_ITEM = (By.XPATH, "//a[@href='#' and text()='Отправить']")
    POSYLKA_OPTION = (By.XPATH, "//a[@href='https://www.pochta.ru/parcels']")


class SendPackageLocators:
    WHERE_SECTION = (
        By.XPATH,
        (
            "//span[@class='SegmentedControlstyles__SegmentedControlContent"
            "-sc-znbens-0 iRXuqE']"
        ),
    )
    INPUT_FIELD = (By.XPATH, "//*[@placeholder]")
