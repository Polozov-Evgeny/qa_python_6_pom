from selenium.webdriver.common.by import By


class HeaderPageLocators:

    SCOOTER_LOGO = [By.XPATH, './/a[@class = "Header_LogoScooter__3lsAR"]/img']
    YANDEX_LOGO = [By.XPATH, './/a[@class = "Header_LogoYandex__3TSOI"]/img']
    DZEN_YANDEX_SEARCH = [By.XPATH, './/div[text() = "Поиск Яндекса"]/parent::div']
