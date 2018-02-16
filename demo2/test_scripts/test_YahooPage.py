import unittest
from selenium import webdriver


class TestVerifyYahooPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://in.yahoo.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        driver.close()

    def test_VerifyLogoPresent(self):
        logo = driver.find_element_by_xpath("//a[@id='uh-logo']")
        self.assertEqual(logo.text, 'Yahoo')

    def test_isupper(self):
        sign_in = driver.find_element_by_xpath("//a[@id='uh-signin']")
        self.assertEqual(sign_in.text, 'Sign in')

if __name__ == '__main__':
    unittest.main()