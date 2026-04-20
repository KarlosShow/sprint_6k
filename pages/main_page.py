import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def click_order_button(self, button_locator):
        with allure.step("Нажать кнопку 'Заказать'"):
            self.click(button_locator)

    def open_faq_answer(self, index: int):
        with allure.step(f"Открыть вопрос FAQ #{index}"):
            self.click(MainPageLocators.FAQ_QUESTION(index))

    def get_faq_answer_text(self, index: int) -> str:
        with allure.step(f"Получить текст ответа FAQ #{index}"):
            return self.find_visible(MainPageLocators.FAQ_ANSWER(index)).text

    def click_scooter_logo(self):
        with allure.step("Нажать на логотип 'Самокат'"):
            self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        with allure.step("Нажать на логотип 'Яндекс'"):
            self.click(MainPageLocators.YANDEX_LOGO)
    def accept_cookies(self):
        cookie_button = self.driver.find_element(By.ID, "rcc-confirm-button")
        cookie_button.click()