from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_INPUT = [By.XPATH, './/input[@placeholder = "* Имя"]']
    SURNAME_INPUT = [By.XPATH, './/input[@placeholder = "* Фамилия"]']
    ADDRESS_INPUT = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']
    METRO_STATION_INPUT = [By.XPATH, './/input[@placeholder = "* Станция метро"]']
    STATION_ITEM = [By.XPATH, './/ul[@class="select-search__options"]//*[text() = "{}"]']
    PHONE_INPUT = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, './/button[text()="Далее"]']

    DELIVERY_DATE_INPUT = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']
    RENTAL_PERIOD_SELECT = [By.XPATH, './/div[text() = "* Срок аренды"]/parent::div//span[@class = "Dropdown-arrow"]']
    RENTAL_PERIOD_ITEM = [By.XPATH, './/div[text() = "{}"]']
    COLOR_CHECKBOX = [By.ID, '{}']
    COMMENT_INPUT = [By.XPATH, './/input[@placeholder = "Комментарий для курьера"]']
    TOTAL_ORDER_BUTTON = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    YES_ORDER_BUTTON = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]']
    TEXT_ORDER_PLACED = [By.XPATH, './/div[text() = "Заказ оформлен"]']
