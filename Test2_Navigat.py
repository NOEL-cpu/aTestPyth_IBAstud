from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def testHw2_Navigation_(browser):
    """ Не стоит разкоментировать т.к не работает, хочется узнать как производить клик по пункту ли  selekt не помогает!!"""
    driver = browser

    # получаем список ссылок в меню About по CSS-селектору
    elems = driver.find_elements_by_css_selector('#downloads ul li a')
    # перебираем полученные подпункты меню,
    # выписываем названия и ссылки в отдельные списки
    # потому что при переходе по ссылкам на другие страницы
    # связь со списком подпунктов будет потеряна
    href_list = []
    name_list = []
    for e in elems:
        href_list.append(e.get_attribute("href"))
        name_list.append(e.get_attribute('innerHTML'))
        print(e.get_attribute("href"))
        print(e.get_attribute('innerHTML'))
        valueStr = "kf"
        valueStr = e.get_attribute('innerHTML')
  #  select.select(e.get_attribute('innerHTML'))
        Select.select_by_value(str(valueStr))

        print("____________")
    # driver.find_element_by_link_text(e.get_attribute("href"))
    # как кликнуть на элемент? хотелосьбы еще переход проверить. или как по ссылке туда пойти.
        time.sleep(3)
    # driver.execute_script("window.history.go(-1)")