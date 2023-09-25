import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class test(unittest.TestCase):
    def test_tc1(self):
        driver=webdriver.Chrome(service=Service("E:\selenium\drivers\chromedriver.exe"))
        self.assertIsNone(driver)# checks driver is None passess tc or fails
        self.assertIsNotNone(driver)# checks driver is not None passess tc or fails


        driver.close()
if __name__ == "__main__":
    unittest.main()