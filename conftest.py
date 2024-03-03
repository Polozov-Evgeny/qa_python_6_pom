import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope='function')
def driver():

    with allure.step('Открываем браузер Firefox'):
        driver = webdriver.Firefox()
        driver.maximize_window()

    yield driver
    with allure.step('Закрываем браузер Firefox'):
        driver.quit()
