import pytest
import allure
from data import Answers
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import driver


class TestMainPage:

    @pytest.mark.parametrize("num, result",
        [
            (0, Answers.ANSWER_1),
            (1, Answers.ANSWER_2),
            (2, Answers.ANSWER_3),
            (3, Answers.ANSWER_4),
            (4, Answers.ANSWER_5),
            (5, Answers.ANSWER_6),
            (6, Answers.ANSWER_7),
            (7, Answers.ANSWER_8)
        ]
    )
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.click_cookie_accept()
        assert main_page.get_answer_text(num) == result
