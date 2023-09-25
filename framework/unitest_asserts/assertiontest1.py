import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class test(unittest.TestCase):
    def test_tc1(self):
        driver=webdriver.Chrome(service=Service("E:\selenium\drivers\chromedriver.exe"))
        driver.get("https://google.com")

        # assertEqual()
        self.assertEqual("Google", driver.title, "title not same")
        # assertNotEqual()
        #self.assertNotEqual("Google", driver.title)
        driver.close()
if __name__ == "__main__":
    unittest.main()