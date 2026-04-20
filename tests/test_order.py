import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL
from data.order_data import ORDER_DATA
from locators.main_page_locators import MainPageLocators


ENTRY_BUTTONS = [
    MainPageLocators.ORDER_BUTTON_TOP,
    MainPageLocators.ORDER_BUTTON_BOTTOM,
]

class TestOrder:

    @allure.title("Заказ самоката: позитивный флоу оформления заказа")
    @pytest.mark.parametrize("entry_button", ENTRY_BUTTONS)
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_flow_positive(self, driver, entry_button, data):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.accept_cookies()
        main.click_order_button(entry_button)
        order = OrderPage(driver)
        order.fill_first_page(data)
        order.fill_second_page(data)
        assert order.success_modal_is_displayed()