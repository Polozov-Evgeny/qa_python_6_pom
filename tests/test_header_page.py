from pages.header_page import HeaderPage
from pages.main_page import MainPage
from data import Data
import allure


class TestHeaderPage:

    @allure.title('Проверка корректности перехода на Главную страницу по нажатию на логотип "Самокат"')
    def test_scooter_logo(self, driver):

        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        header_page.go_to_url(Data.ORDER_PAGE_URL)
        header_page.click_on_scooter_logo()

        assert main_page.check_is_main_page(header_page.get_current_url()), \
            'Возникла проблема при переходе на главную страницу "Самоката"'


    @allure.title('Проверка корректности перехода на страницу "Дзен" по нажатию на логотип "Яндекс"')
    def test_yandex_logo(self, driver):

        header_page = HeaderPage(driver)
        header_page.go_to_url(Data.MAIN_PAGE_URL)
        header_page.click_on_yandex_logo()
        header_page.switch_to_browser_tab(1)

        assert header_page.check_is_dzen_page(), \
            'Возникла проблема при переключении на страницу "Дзен"'
