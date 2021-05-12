import unittest

def setUpModule(): #executed before executing any class
    print("setUpModule")

def tearDownModule(): #executed after completing everything in python module
    print("tearDownModule")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self): #Execute before all the test methods
        print("This is login test")
    @classmethod
    def tearDown(self): #Execute ofter all the test methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls): #Execute once when the class is started
        print("open application")

    @classmethod
    def tearDownClass(cls): #Execute once when the class is completed
        print("close application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")

if __name__ == "__main__":
    unittest.main()