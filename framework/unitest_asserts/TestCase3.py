import unittest
from selenium import webdriver

def setUpModule():# will be executed before executing any class or any method present in the test class
    print("setup module")

def tearDownModule():# will be executed after completing everything present in the python module
    print("TearDown module")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):# executed before all the class method
        print("this is login test")
    @classmethod
    def tearDown(self):# executed after all the class method
        print("this is logout test")

    @classmethod
    def setUpClass(cls):# executed once when the class method started
        print("opening the application")

    @classmethod
    def tearDownClass(cls):# executed once when the class method completed
        print("Closing the application")

    def test_search(self):
        print("this is the search test")

    def test_advancedserach(self):
        print("this is the advanced search test")

    def test_prepaidrecharge(self):
        print("this is the prepaid recharge test")

    def test_postpaidrecharge(self):
        print("this is the postpaid recharge test")

if __name__ == "__main__":
    unittest.main()