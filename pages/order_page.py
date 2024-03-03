from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage, OrderPageLocators):

    def set_metro_station(self, name_station):
        self.click_on_element_with_wait(self.METRO_STATION_INPUT)
        method, station_loc = self.STATION_ITEM
        station_locator_with_name = (method, station_loc.format(name_station))
        self.scroll_to_element(station_locator_with_name)
        self.click_on_element_with_wait(station_locator_with_name)

    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_in_form_for_whom_scooter(self, name, surname, address, name_station, phone):
        self.set_text_to_element_with_wait(self.NAME_INPUT, name)
        self.set_text_to_element_with_wait(self.SURNAME_INPUT, surname)
        self.set_text_to_element_with_wait(self.ADDRESS_INPUT, address)
        self.set_metro_station(name_station)
        self.set_text_to_element_with_wait(self.PHONE_INPUT, phone)
        self.click_on_element_with_wait(self.NEXT_BUTTON)

    def set_rental_period(self, rental_period):
        self.click_on_element_with_wait(self.RENTAL_PERIOD_SELECT)
        method, period_loc = self.RENTAL_PERIOD_ITEM
        rent_locator_with_period = (method, period_loc.format(rental_period))
        self.scroll_to_element(rent_locator_with_period)
        self.click_on_element_with_wait(rent_locator_with_period)

    def set_scooter_color(self, scooter_color):
        method, checkbox_loc = self.COLOR_CHECKBOX
        checkbox_locator_with_color = (method, checkbox_loc.format(scooter_color))
        self.click_on_element_with_wait(checkbox_locator_with_color)

    @allure.step('Заполняем форму "Про аренду"')
    def fill_in_form_about_rent(self, date, rental_period, scooter_color, comment):
        self.set_text_to_element_with_wait(self.DELIVERY_DATE_INPUT, date)
        self.set_rental_period(rental_period)
        self.set_scooter_color(scooter_color)
        self.set_text_to_element_with_wait(self.COMMENT_INPUT, comment)
        self.click_on_element_with_wait(self.TOTAL_ORDER_BUTTON)

    @allure.step('Соглашаемся на оформление заказа и проверяем, что он оформлен')
    def click_yes_and_get_text_order_placed(self):
        self.click_on_element_with_wait(self.YES_ORDER_BUTTON)
        actual_result = self.get_text_from_element_with_wait(self.TEXT_ORDER_PLACED)
        return actual_result
