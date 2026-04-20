import allure
from data.urls import BASE_URL, DZEN_URL_PART
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogos:

    @allure.title("Логотип Самоката ведёт на главную страницу Самоката")
    def test_scooter_logo_opens_home(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.accept_cookies()
        page.click_order_button(MainPageLocators.ORDER_BUTTON_TOP)
        page.click_scooter_logo()
        assert page.get_current_url() == BASE_URL

    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.accept_cookies()
        page.click_yandex_logo()
        page.switch_to_last_window()
        WebDriverWait(driver, 10).until(
        EC.url_contains(DZEN_URL_PART)
        )
        assert DZEN_URL_PART in page.get_current_url()