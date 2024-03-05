from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def is_element_displayed_with_wait(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    def click_on_element_with_wait(self, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element_with_wait(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element_with_wait(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_url(self, url):
        with allure.step(f'Открываем страницу {url}'):
            self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_browser_tab(self, number):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[number])
