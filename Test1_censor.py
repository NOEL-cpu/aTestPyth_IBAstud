from fixtures import *
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def test_censors(browser):
    driver=browser
    # получение элемента страницы с именем
    elem = driver.find_element_by_xpath("//*[@id='id-search-field']")
    # ввод в этот элемент какйто байды
    elem.send_keys("сурок")
    time.sleep(1)
    elem.send_keys(Keys.ENTER)
    time.sleep(2)
    # 1 ый способ откатится на предыдущую страницу
    driver.back()
    time.sleep(3)
    a = "Он"
    # Проверка поведения поля при большом количестве символов
    for i in range(0, 5):
        a = a + "Урюк "
        elem = driver.find_element_by_xpath("//*[@id='id-search-field']")
        elem.send_keys(a)
        time.sleep(1)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        print(str(i))
        elem = driver.find_elements_by_xpath("//html/body/div/div[3]/div/section/form/ul/p")
        elem = driver.find_element_by_tag_name("p")
        print ("!!!!!!!!!!!!"+ str(elem))
     #   assert "No results found." == elem.text.find("No results found.")
   #     assert 1 == 1
        assert elem.text.find("No results found.") >= 0
        # Второй способ откатится назад на одну страницу
        driver.execute_script("window.history.go(-1)")
        time.sleep(2)
