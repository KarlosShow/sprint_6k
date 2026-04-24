import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        with allure.step(f"Открыть страницу: {url}"):
            self.driver.get(url)

    def find_visible(self, locator):
        with allure.step(f"Найти видимый элемент: {locator}"):
            return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        with allure.step(f"Найти кликабельный элемент: {locator}"):
            return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            self.find_clickable(locator).click()

    def type(self, locator, value: str):
        with allure.step(f"Ввести '{value}' в поле: {locator}"):
            el = self.find_visible(locator)
            el.clear()
            el.send_keys(value)
            return el

    def get_current_url(self) -> str:
        with allure.step("Получить текущий URL"):
            return self.driver.current_url

    def switch_to_last_window(self):
        with allure.step("Переключиться на последнюю вкладку"):
            self.driver.switch_to.window(self.driver.window_handles[-1])



    def scroll_to_bottom(self):
        with allure.step("Прокрутить страницу вниз"):
            self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def scroll_to_element(self, element):
        with allure.step("Прокрутить к элементу"):
            self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def find_all(self, locator):
        with allure.step(f"Найти все элементы: {locator}"):
            return self.driver.find_elements(*locator)

    def wait_for_elements(self, locator):
        with allure.step(f"Дождаться появления элементов: {locator}"):
            return self.wait.until(
            lambda d: len(d.find_elements(*locator)) > 0
        )