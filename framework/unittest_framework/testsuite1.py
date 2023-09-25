import unittest

from package1.ts_login import Testlogin
from package1.ts_signup import TestSignup

from package2.ts_refund import TestRefund
from package2.ts_payment import TestPayment

# get all test cases from testlogin, test signup, testrefund, testpayment
tc1=unittest.TestLoader().loadTestsFromTestCase(Testlogin)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestSignup)
tc3=unittest.TestLoader().loadTestsFromTestCase(TestPayment)
tc4=unittest.TestLoader().loadTestsFromTestCase(TestRefund)

# create the test suite
sanity = unittest.TestSuite([tc1,tc2])
functionality = unittest.TestSuite([tc3,tc4])
master = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner(verbosity=2).run(master)