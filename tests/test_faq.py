import pytest
import allure
# from locators import main_page_locators
from pages.main_page import MainPage
from data.urls import BASE_URL
from data.faq_data import FAQ_CASES

class TestFAQ:
    @allure.title("Проверка открытия ответа в FAQ")
    @pytest.mark.parametrize("index, expected_part", FAQ_CASES)
    def test_faq_answer_opens(self, main_page, index, expected_part):

        main_page.open_faq_answer(index)

        answer_text = main_page.get_faq_answer_text(index)

        assert expected_part in answer_text