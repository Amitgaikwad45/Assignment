#Relational comparison assertGreater
# assertIn assertNotIn
import unittest

class Test(unittest.TestCase):
    def test_Name(self):
        list={"python","selenium","java"}
        self.assertIn("python",list) #passed
        self.assertIn("ruby",list)   #failed
        self.assertNotIn("ruby",list) #passed
        self.assertNotIn("python",list) #failed
        self.assertGreater(100,10) #compare for 100>10 then test passed
        self.assertGreaterEqual(100,100) #checks 100>=100 if matches test passed
        self.assertLess(10,10) #fail the test because 10 is not less than 10
        self.assertLessEqual(10,100) #first num should be less than or eaual to second number

if __name__ == "__main__":
    unittest.main()