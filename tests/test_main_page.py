import pytest
from pages.main_page import MainPage
from data import Data
import allure


class TestMainPage:

    @allure.title('Проверка корректности блока с ответами на Главной странице')
    @allure.description('В рамках проверки сверяется фактическое значение ответа с его ожидаемым результатом')
    @pytest.mark.parametrize(
        'q_a_number, expected_result',
        [
            (0, Data.ANSWERS[0]),
            (1, Data.ANSWERS[1]),
            (2, Data.ANSWERS[2]),
            (3, Data.ANSWERS[3]),
            (4, Data.ANSWERS[4]),
            (5, Data.ANSWERS[5]),
            (6, Data.ANSWERS[6]),
            (7, Data.ANSWERS[7])

        ]
    )
    def test_check_answers(self, driver, q_a_number, expected_result):

        main_page = MainPage(driver)
        main_page.go_to_url_and_click_on_cookies_button()
        actual_result = main_page.click_to_question_and_get_answer_text(
            q_a_number
        )

        assert main_page.check_answer(actual_result, expected_result), \
            f'Фактический вопрос "{actual_result}" не соответствует ожидаемому "{expected_result}"'
