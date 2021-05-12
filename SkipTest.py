import unittest
class AppTesting(unittest.TestCase):
    @unittest.SkipTest #decorator
    def test_search(self):
        print("This is search test")
    @unittest.skip("skipping this test because it is not ready")
    def test_advancedsearch(self):
        print("This is advanced search test")
    @unittest.skipIf(1==1,"one is equal to one")
    def test_prepaidRecharge(self):
        print("This is prepaid recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")

    def test_loginbygmail(self):
        print("login by gmail")

    def test_loginbytwitter(self):
        print("login by twitter")

if __name__ == "__main__":
    unittest.main()
