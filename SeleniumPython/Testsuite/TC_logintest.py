import unittest
class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("login by email test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("login by facebook test")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("login by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

