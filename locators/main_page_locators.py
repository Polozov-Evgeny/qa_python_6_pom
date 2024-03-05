from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIES_BUTTON = [By.ID, 'rcc-confirm-button']
    QUESTION_ITEM = [By.ID, 'accordion__heading-{}']
    TEXT_ANSWER_ITEM = [By.XPATH, './/div[@id = "accordion__panel-{}"]/p']
    MAIN_ORDER_BUTTON = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text() = "Заказать"]']
    HEADER_ORDER_BUTTON = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']
    SCOOTER_BANNER_TEXT = [By.XPATH, './/div[@class="Home_Header__iJKdX"]']
