from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from data import Data
import allure


class HeaderPage(BasePage, HeaderPageLocators):

    @allure.step('Нажимаем на кнопку "Заказать" в заголовке страницы')
    def click_on_order_button(self):
        self.click_on_element_with_wait(self.ORDER_BUTTON)

    @allure.step('Нажимаем на логотип "Самокат" в заголовке страницы')
    def click_on_scooter_logo(self):
        self.click_on_element_with_wait(self.SCOOTER_LOGO)

    @allure.step('Нажимаем на логотип "Яндекс" в заголовке страницы')
    def click_on_yandex_logo(self):
        self.click_on_element_with_wait(self.YANDEX_LOGO)

    @allure.step('Проверяем открытие страницы "Дзен"')
    def check_is_dzen_page(self):
        self.find_element_with_wait(self.DZEN_YANDEX_SEARCH)
        url = self.get_current_url()
        return (Data.DZEN_PAGE_URL in url and
                self.is_element_displayed_with_wait(self.DZEN_YANDEX_SEARCH))
