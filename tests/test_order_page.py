import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import Data
import allure


class TestOrderPage:

    @allure.title('Проверка корректности оформления заказа')
    @allure.description('Проверяется 2 точки входа, корректность заполнения полей формы и оформление заказа')
    @pytest.mark.parametrize('order_data_set', [Data.order_data_set1, Data.order_data_set2])
    def test_make_an_order(self, driver, order_data_set):

        main_page = MainPage(driver)
        main_page.go_to_url_and_click_on_cookies_button()
        main_page.select_order_button(order_data_set['place_order_btn'])

        order_page = OrderPage(driver)
        order_page.fill_in_form_for_whom_scooter(order_data_set)
        order_page.fill_in_form_about_rent(order_data_set)
        actual_result = order_page.click_yes_and_get_text_order_placed()
        assert 'Заказ оформлен' in actual_result, 'Возникла проблема при оформлении заказа'
