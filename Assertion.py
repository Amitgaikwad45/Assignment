#asserttrue assertfalse assertnone assertnotnone
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_Name(self):
        driver=webdriver.Chrome(executable_path='F:/chromedriver.exe')
        #driver = None
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)
        driver.get("https://www.google.com/")
        titleofpage=driver.title


        #assertequal
        self.assertEqual("Google",titleofpage,"webpage title is not same")
        #assertnotequal
        self.assertNotEqual("Google123",titleofpage)
        self.assertTrue(titleofpage=="Google12")#true
        self.assertFalse(titleofpage=="Google12")



if __name__ == "__main__":
    unittest.main()