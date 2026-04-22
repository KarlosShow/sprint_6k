import pytest
import allure
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
