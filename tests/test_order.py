import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import BASE_URL
from data.order_data import BUTTON_DATA_PAIRS  # импорт из обновлённого файла
from locators.main_page_locators import MainPageLocators

class TestOrder:
    @allure.title("Заказ самоката: позитивный флоу оформления заказа")
    @pytest.mark.parametrize("button_name, order_data", BUTTON_DATA_PAIRS)
    def test_order_flow_positive(self, main_page, button_name, order_data):
        # Получаем локатор кнопки по имени
        entry_button = getattr(MainPageLocators, button_name)

        main_page.click_order_button(entry_button)

        order = OrderPage(main_page.driver)
        order.fill_first_page(order_data)
        order.fill_second_page(order_data)

        assert order.success_modal_is_displayed()