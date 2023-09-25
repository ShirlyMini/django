import unittest

class test(unittest.TestCase):
    def test_tc1(self):

        # assertGreater()
        #self.assertGreater(500,300) # passes
        #self.assertGreater(300,500) # Fails


        # assertGreaterEqual()
        # self.assertGreaterEqual(500, 300)
        # self.assertGreaterEqual(500, 500)

        # assertLesser()
        self.assertLess(300, 500)
        #self.assertLessEqual(300, 500)
        #self.assertLessEqual(500, 500)


if __name__ == "__main__":
    unittest.main()