from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g')]")
    FAQ_QUESTION = lambda index: (By.ID, f"accordion__heading-{index}")
    FAQ_ANSWER = lambda index: (By.ID, f"accordion__panel-{index}")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    COOCIE_BUTTON = (By.XPATH, "//button[contains(@class, 'App_CookieButton__3cvqF')]")

