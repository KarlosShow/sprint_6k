from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = lambda text: (By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{text}']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")
    RENT_OPTION = lambda text: (By.XPATH, f"//div[contains(@class,'Dropdown-menu')]//div[text()='{text}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать')]")
    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    SUCCESS_TITLE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(text(),'Заказ оформлен')]")