# **Тема "Page Object" курс ЯндексПрактикум**

### Проект автоматизации тестирования сайта "Яндекс.Самокат"

1. Ссылка на сайт: *https://qa-scooter.praktikum-services.ru/*
2. Автотесты подключены в браузере: *Firefox*
3. Основа для написания автотестов: *Selenium WebDriver* и *Pytest*
4. В автотестах используются: паттерн *POM*, фикстуры *@pytest.fixture* и параметризация *@pytest.mark.parametrize*
5. Отчет о тестировании: *Allure*

**Установка Pytest:**
````
pip install pytest
````

**Установка Selenium:**
````
pip install selenium
````

**Запуск автотестов:**
````
pytest -v
````

**Отчет о тестировании Allure:**
````
pytest tests --alluredir=allure_results
````
````
allure serve allure_results
````