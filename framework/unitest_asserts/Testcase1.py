import unittest


class Test(unittest.TestCase):
    # test method start with text_ prefix
    def test_firstTest(self):
        print("this is my first unit test case")


if __name__ == "__main__":
    unittest.main()
