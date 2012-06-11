#Drag and drop function is pending.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnStoreHierarchyFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_store_hierarchy_function_drag_and_drop(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/storehierarchy")
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='hierarchy_company"+storeHierarchyCompanyID+"']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='hierarchy_storeGroup"+storeHierarchyStoreGroupID+"']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='hierarchy_store"+storeHierarchyStoreID+"']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [dragAndDropToObject]]
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='hierarchy_storeGroup"+storeHierarchyStoreGroupID+"']/div/div[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [dragAndDropToObject]]
        driver.refresh()
#        driver.find_element_by_link_text("Group Media Players").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
