import unittest

class test(unittest.TestCase):
    def test_tc1(self):
        lst1=["python", "selenium", "java", "robot"]

        # assertIn()
        #self.assertIn("python", lst1, "list contains the value") # passed
        #self.assertIn("python123", lst1, "list contains the value") # fails
        # assertNotIn()
        #self.assertNotIn("python", lst1, "list doesnt contains the value")
        self.assertNotIn("python123", lst1, "list doesnt contains the value")


if __name__ == "__main__":
    unittest.main()