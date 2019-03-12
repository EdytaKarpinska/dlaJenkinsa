import unittest
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mewe.com')
        self.driver.maximize_window()

    def test_login(self):
        self.driver.find_element_by_id("login-fake-btn").click()
        self.driver.find_element_by_id("email").send_keys("edyta.karpinska@wp.pl")
        self.driver.find_element_by_id("password").send_keys("besttester87")
        self.driver.find_element_by_xpath("//button[text()='Log in']").click()
        self.driver.find_element_by_id('content-wrapper')

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()