import unittest
class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("signup by email test")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("signup by facebook test")
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print("signup by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()

