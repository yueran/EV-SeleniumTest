from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnTemplateStyleFunctionSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_template_style_function_search(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/templatestyles")
        driver.find_element_by_css_selector("span.searchIcon").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        driver.find_element_by_id("templateSearch").clear()
        driver.find_element_by_id("templateSearch").send_keys("qq")
        driver.find_element_by_css_selector("span.searchIcon").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
