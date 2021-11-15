import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import key_actions
from selenium.webdriver.support.ui import Select
from fixtures import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def test4_breadcrumbs3(browser):
    """Работоспособность всех ссылок"""

    driver=browser
    #  в скобках иерархия? id которая содержит li и у этих li есть a???по какой логике задаются . menu li???  почему хлебные крошки
    elems = driver.find_elements_by_css_selector('#mainnav li a')
    # как проверить по названию класса или id который содержит два и более слов
    href_list = []
    article_list = []
    print(elems)
    print("hhhhhhhh")
    for e in elems:
        href_list.append(e.get_attribute("href"))
        article_list.append(e.get_attribute('innerHTML'))

    # Проверяем наличие страниц
    for i in range(len(href_list)):
        driver.get(href_list[i])

        time.sleep(1)
        print(str(i) + " " + article_list[i] + " " + href_list[i])