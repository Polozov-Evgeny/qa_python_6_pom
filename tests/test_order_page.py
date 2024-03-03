import pytest
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.header_page import HeaderPage
from data import Data
import allure


class TestOrderPage:

    @allure.title('Проверка корректности оформления заказа')
    @allure.description('Проверяется 2 точки входа, корректность заполнения полей формы и оформление заказа')
    @pytest.mark.parametrize(
        'place_order_btn, name, surname, address, name_station, phone, date, rental_period, scooter_color, comment',
        [
            (
                'main',
                'Евгений',
                'Сазанов',
                'г.Нижний Новгород, ул.Новая, д.15, кв.99',
                Data.NAME_STATION[0],
                '89051117890',
                '21.03.2024',
                Data.RENTAL_PERIOD[0],
                Data.SCOOTER_COLOR[0],
                'Предварительно позвонить по телефону'
            ),
            (
                'header',
                'максим',
                'крылов',
                'МОСКВА ПУШКИНА 21-3',
                Data.NAME_STATION[1],
                '+79051112233',
                '27.04.2024',
                Data.RENTAL_PERIOD[1],
                Data.SCOOTER_COLOR[1],
                ''
            )
        ]
    )
    def test_make_an_order(
            self, driver, place_order_btn, name, surname, address,
            name_station, phone, date, rental_period, scooter_color, comment
    ):

        main_page = MainPage(driver)
        main_page.go_to_url_and_click_on_cookies_button()
        if place_order_btn == 'main':
            main_page.click_on_order_button()
        else:
            header_page = HeaderPage(driver)
            header_page.click_on_order_button()

        order_page = OrderPage(driver)
        order_page.fill_in_form_for_whom_scooter(name, surname, address, name_station, phone)
        order_page.fill_in_form_about_rent(date, rental_period, scooter_color, comment)
        actual_result = order_page.click_yes_and_get_text_order_placed()
        assert 'Заказ оформлен' in actual_result, 'Возникла проблема при оформлении заказа'
