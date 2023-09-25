import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class test(unittest.TestCase):
    def test_tc1(self):
        driver=webdriver.Chrome(service=Service("E:\selenium\drivers\chromedriver.exe"))
        driver.get("https://google.com")
        titleOfWebPage=driver.title
        # assertTrue
        #self.assertTrue(titleOfWebPage=="Google") # passes the test case
        #self.assertTrue(titleOfWebPage=="Google123") # fails the test case
        # assertFalse
        #self.assertFalse(titleOfWebPage == "Google123") # passes the test case condtion return False also excepting false
        self.assertFalse(titleOfWebPage == "Google") # fails the test case condtion return true but excepting false



        driver.close()
if __name__ == "__main__":
    unittest.main()