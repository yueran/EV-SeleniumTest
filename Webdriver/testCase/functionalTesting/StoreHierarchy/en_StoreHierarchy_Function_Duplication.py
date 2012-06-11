#The duplicated company needs more time to show up. 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnStoreHierarchyFunctionDuplication(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_store_hierarchy_function_duplication(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/storehierarchy")
        try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyDuplicateStore, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyCompanyCopy, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroupCopy, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyDuplicateStoreCopy, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#Flexible
        try: self.assertTrue(self.is_element_present(By.ID, "hierarchy_company"+storeHierarchyCompanyID+"Duplicate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "hierarchy_storeGroup"+storeHierarchyStoreGroupID+"Duplicate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "hierarchy_store"+storeHierarchyDuplicateStoreID+"Duplicate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
#        driver.find_element_by_id("hierarchy_company"+storeHierarchyCompanyID+"Duplicate").click()
#        self.driver.implicitly_wait(30000)
#        driver.find_element_by_id("hierarchy_storeGroup"+storeHierarchyStoreGroupID+"Duplicate").click()
#        self.driver.implicitly_wait(30000)
        driver.find_element_by_id("hierarchy_store"+storeHierarchyDuplicateStoreID+"Duplicate").click()
        #page load problem
        self.driver.implicitly_wait(30000)
        driver.refresh()
        driver.find_element_by_id("hierarchy_storeGroup"+storeHierarchyStoreGroupID+"Duplicate").click()
        self.driver.implicitly_wait(30000)
        driver.refresh()
        driver.find_element_by_id("hierarchy_company"+storeHierarchyCompanyID+"Duplicate").click()
        self.driver.implicitly_wait(30000)
        driver.refresh()
        self.driver.implicitly_wait(30000)
        try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyCompanyCopy, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroupCopy, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyDuplicateStoreCopy, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
