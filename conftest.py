import pytest
from selenium import webdriver
from pages.main_page import MainPage
from data.urls import BASE_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    page.accept_cookies()
    return page