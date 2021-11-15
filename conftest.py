import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

# фикстура для запуска браузера перед тестом и закрытия после теста
@pytest.fixture()
def browser():
    # запуск Firefox при начале каждого теста (до yield)
    driver = webdriver.Firefox()
    # открытие страницы при начале каждого теста
    page = driver.get('http://www.python.org')
    # передача драйвера для использования в тесте
    yield driver
    # закрытие браузера после теста (после yield)
   # driver.close()

# фикстура для выбора русского языка после запуска браузера
# (название фикстуры browser передано в параметре)

