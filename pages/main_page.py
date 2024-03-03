from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Data
import allure


class MainPage(BasePage, MainPageLocators):

    @allure.step('Переходим на Главную страницу и подтверждаем куки')
    def go_to_url_and_click_on_cookies_button(self):
        self.go_to_url(Data.MAIN_PAGE_URL)
        self.click_on_element_with_wait(self.COOKIES_BUTTON)

    @allure.step('Нажимаем на вопрос и получаем текст его ответа')
    def click_to_question_and_get_answer_text(self, number):
        method, question_loc = self.QUESTION_ITEM
        question_locator_with_number = (method, question_loc.format(number))
        self.scroll_to_element(question_locator_with_number)
        self.click_on_element_with_wait(question_locator_with_number)

        method, answer_loc = self.TEXT_ANSWER_ITEM
        answer_locator_with_number = (method, answer_loc.format(number))
        return self.get_text_from_element_with_wait(answer_locator_with_number)

    @staticmethod
    @allure.step('Сравниваем фактически полученный ответ с ожидаемым')
    def check_answer(actual_result, expected_result):
        return actual_result == expected_result

    @allure.step('Нажимаем на кнопку "Заказать" на Главной странице')
    def click_on_order_button(self):
        self.scroll_to_element(self.ORDER_BUTTON)
        self.click_on_element_with_wait(self.ORDER_BUTTON)

    @allure.step('Проверяем открытие Главной страницы')
    def check_is_main_page(self, url):
        return (Data.MAIN_PAGE_URL == url and
                'Самокат' in self.get_text_from_element_with_wait(self.SCOOTER_BANNER_TEXT))