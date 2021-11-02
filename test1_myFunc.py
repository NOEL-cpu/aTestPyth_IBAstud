import unittest
from myFunc import*




class MyTestCase(unittest.TestCase):

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
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after [" + self.shortDescription() + "]")

    def test_1something(self):
        """11111111111"""
        print("test id: " + self.id())
        print('tlen_test')
        self.assertEqual(tlen("Дирижабль"), 9)  # add assertion here

    def test_2hypotenuse(self):
        """2222222222"""
        print('hyp_test')
        print("test id: " + self.id())
        self.assertEqual(hypotenuse(3, 4), 5)  # add assertion here

    def test_3ipAddress(self):
        """33333333"""
        print("test id: " + self.id())
        ip = "192.168.56.1"
        self.assertEqual(ipadress(),ip)
