import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    def fill_first_page(self, data: dict):
        with allure.step("Заполнить первую страницу заказа"):

            self.type(OrderPageLocators.NAME, data["name"])
            self.type(OrderPageLocators.SURNAME, data["surname"])
            self.type(OrderPageLocators.ADDRESS, data["address"])

            self.click(OrderPageLocators.METRO)
            self.click(OrderPageLocators.METRO_OPTION(data["metro"]))

            self.type(OrderPageLocators.PHONE, data["phone"])

            self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_page(self, data: dict):
        with allure.step("Заполнить вторую страницу заказа"):

            # Дата
            date_input = self.find_clickable(OrderPageLocators.DATE)
            date_input.click()
            self.type(OrderPageLocators.DATE, data["date"])
            date_input.send_keys(Keys.RETURN)

            # Срок аренды
            self.click(OrderPageLocators.RENT)
            self.click(OrderPageLocators.RENT_OPTION(data["rent"]))

            # Цвет
            with allure.step("Выбрать цвет самоката"):
                color = data["color"].lower()
                if color == "black":
                    self.click(OrderPageLocators.COLOR_BLACK)
                elif color == "grey":
                    self.click(OrderPageLocators.COLOR_GREY)
                else:
                    raise ValueError(f"Неизвестный цвет: {color}")

            # Комментарий
            self.type(OrderPageLocators.COMMENT, data["comment"])

            # Заказать
            self.click(OrderPageLocators.ORDER_BUTTON)

            # Подтверждение
            self.click(OrderPageLocators.CONFIRM_YES)

    def success_modal_is_displayed(self) -> bool:
        with allure.step("Проверить, что появилось окно успешного заказа"):
            return self.find_visible(OrderPageLocators.SUCCESS_TITLE).is_displayed()