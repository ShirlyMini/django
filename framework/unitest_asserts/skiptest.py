import unittest
from selenium import webdriver

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("this is the search test")

    @unittest.skip("skipping this test method because it is underdeveloped")
    def test_advancedserach(self):
        print("this is the advanced search test")

    @unittest.skipIf(1==1, "condition is True")# True
    def test_prepaidrecharge(self):
        print("this is the prepaid recharge test")

    def test_postpaidrecharge(self):
        print("this is the postpaid recharge test")

    def test_loginbygmail(self):
        print("this is the login by gmail test")\

    def test_loginbyfb(self):
        print("this is the login by facebook test")



if __name__ == "__main__":
    unittest.main()