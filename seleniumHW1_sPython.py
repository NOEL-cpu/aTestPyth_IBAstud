import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import key_actions
from selenium.webdriver.support.ui import Select


class PythonOrgSearch(unittest.TestCase):
    """Как сделать метод который будет выбирать какой метод выполнять а то коментировать надоелао"""
    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up some stuff for [" + self.shortDescription() + "]")
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        """Tear Down Method!"""
        self.driver.close()


    def testHw1_search_in_python_org(self):
        """Проверка на Ввод в поле поиска неприличных слов и проверка отсутсвия результата поиска"""
        driver = self.driver
        # открытие в chrome страницы http://www.python.org
        driver.get("http://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # ждем 5 секунд
        time.sleep(2)
        # получение элемента страницы с именем
        elem = driver.find_element_by_xpath("//*[@id='id-search-field']")
        #ввод в этот элемент какйто байды
        elem.send_keys("сурок")
        time.sleep(1)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        # 1 ый способ откатится на предыдущую страницу
        driver.back()
        time.sleep(3)
        a = "Он"
        #Проверка поведения поля при большом количестве символов
        for i in range(0, 5):
            a = a + "Урюк "
            elem = driver.find_element_by_xpath("//*[@id='id-search-field']")
            elem.send_keys(a)
            time.sleep(1)
            elem.send_keys(Keys.ENTER)
            time.sleep(2)
            print(str(i))
            elem = driver.find_element_by_css_selector('p')
            self.assertIn("No results", driver.page_source)
            #Второй способ откатится назад на одну страницу
            driver.execute_script("window.history.go(-1)")
            time.sleep(2)

    # def testHw2_Navigation_(self):
    #""" Не стоит разкоментировать т.к не работает, хочется узнать как производить клик по пункту ли  selekt не помогает!!"""
        # driver = self.driver
        # # открытие в Firefox страницы http://www.python.org
        # driver.get("http://www.python.org")
        # # получаем список ссылок в меню About по CSS-селектору
        # elems = driver.find_elements_by_css_selector('#downloads ul li a')
        # # перебираем полученные подпункты меню,
        # # выписываем названия и ссылки в отдельные списки
        # # потому что при переходе по ссылкам на другие страницы
        # # связь со списком подпунктов будет потеряна
        # href_list = []
        # name_list = []
        # for e in elems:
        # href_list.append(e.get_attribute("href"))
        # name_list.append(e.get_attribute('innerHTML'))
        # print(e.get_attribute("href"))
        # print(e.get_attribute('innerHTML'))
        # valueStr = "kf"
        # valueStr = e.get_attribute('innerHTML')
        # select.select(e.get_attribute('innerHTML'))
        # Select.select_by_value(str(valueStr))
        #
        # print("____________")
        # #driver.find_element_by_link_text(e.get_attribute("href"))
        # # как кликнуть на элемент? хотелосьбы еще переход проверить. или как по ссылке туда пойти.
        # time.sleep(3)
        # # driver.execute_script("window.history.go(-1)")



    # def test4_breadcrumbs3(self):
    #     """Работоспособность всех ссылок"""
    #     driver = self.driver
    #     # открытие в Chrome страницы http://www.python.org
    #     driver.get("http://www.python.org")
    #     #  в скобках иерархия? id которая содержит li и у этих li есть a???по какой логике задаются . menu li???  почему хлебные крошки
    #     elems = driver.find_elements_by_css_selector('#mainnav li a')
    #     # как проверить по названию класса или id который содержит два и более слов
    #     href_list = []
    #     article_list = []
    #     print (elems)
    #     print("hhhhhhhh")
    #     for e in elems:
    #         href_list.append(e.get_attribute("href"))
    #         article_list.append(e.get_attribute('innerHTML'))
    #
    #
    #     # Проверяем наличие страниц
    #     for i in range(len(href_list)):
    #         driver.get(href_list[i])
    #
    #         time.sleep(1)
    #         print(str(i)+ " "+article_list[i]+" " + href_list[i] )


if __name__ == '__main__':
    unittest.main()