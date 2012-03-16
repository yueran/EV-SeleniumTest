from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnScheduleTemplatesFunctionSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_schedule_templates_function_search(self):
        driver = self.driver
        # This is manually test pass. But here it seems to be a false negative.
        driver.get(self.base_url + "/ev/scheduletemplates")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt]]
        driver.find_element_by_id("filterTemplateText").clear()
        driver.find_element_by_id("filterTemplateText").send_keys("t")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("filterTemplateText").clear()
        driver.find_element_by_id("filterTemplateText").send_keys("te")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("filterTemplateText").clear()
        driver.find_element_by_id("filterTemplateText").send_keys("tes")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("filterTemplateText").clear()
        driver.find_element_by_id("filterTemplateText").send_keys("")
        try: self.assertTrue(self.is_element_present(By.ID, "filterTemplateText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("filterStoreText").clear()
        driver.find_element_by_id("filterStoreText").send_keys("test")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
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
