from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnStoreHierarchyFunctionModification(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_store_hierarchy_function_modification(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/storehierarchy")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("hierarchy_company179Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("modifyCompany")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_storeGroup180Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("modifyStoreGroup")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_store181Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("modifyStore")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_css_selector("button.exit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.refresh()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("hierarchy_company179Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("MtestC")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_storeGroup180Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("MtestG")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_store181Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("MtestS")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_css_selector("button.exit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
