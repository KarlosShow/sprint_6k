import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
class OrderPage(BasePage):
    def fill_first_page(self, data: dict):
        with allure.step("Заполнить первую страницу заказа"):
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.NAME)
            )
            self.type(OrderPageLocators.NAME, data["name"])
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.SURNAME)
            )  
            self.type(OrderPageLocators.SURNAME, data["surname"])
            self.type(OrderPageLocators.ADDRESS, data["address"])
            self.click(OrderPageLocators.METRO)
            self.click(OrderPageLocators.METRO_OPTION(data["metro"]))
            self.type(OrderPageLocators.PHONE, data["phone"])
            self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_page(self, data: dict):
        with allure.step("Заполнить вторую страницу заказа"):

            date_input = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(OrderPageLocators.DATE)
        )
        date_input.click()
        self.type(OrderPageLocators.DATE, data["date"])
        date_input.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.RENT)
        ).click()

        rent_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.RENT_OPTION(data["rent"]))
        )
        rent_option.click()

        with allure.step("Выбрать цвет самоката"):
            color = data["color"].lower()
            if color == "black":
                self.click(OrderPageLocators.COLOR_BLACK)
            elif color == "grey":
                self.click(OrderPageLocators.COLOR_GREY)
            else:
                raise ValueError(f"Неизвестный цвет: {color}")

        self.type(OrderPageLocators.COMMENT, data["comment"])

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_YES)
        ).click()

    def success_modal_is_displayed(self) -> bool:
        with allure.step("Проверить, что появилось окно успешного заказа"):
            return self.find_visible(OrderPageLocators.SUCCESS_TITLE).is_displayed()