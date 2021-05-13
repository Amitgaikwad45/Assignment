import unittest
from Package1.TC_logintest import LoginTest
from Package1.TC_signup import SignupTest
from Package2.TC_payment import PaymentTest
from Package2.Paymentreturntest import PaymentRetTest

#get all test from LoginTest,SignupTest,paymentTest,PaymentReturnTest
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentRetTest)

#master test suite is combination of sanity test suite and functional test suite

#creating the test suite
sanitytestsuite=unittest.TestSuite([tc1,tc2]) #sanity test suite
#unittest.TextTestRunner().run(sanitytestsuite)
functionaltestsuite=unittest.TestSuite([tc3,tc4])
mastertestsuite=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(functionaltestsuite)