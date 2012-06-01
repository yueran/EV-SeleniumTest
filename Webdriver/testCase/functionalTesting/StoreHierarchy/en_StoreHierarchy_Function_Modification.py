from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnStoreHierarchyFunctionModification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_store_hierarchy_function_modification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/storehierarchy")
        #id:EditCompany: 340 #EditStoreGroup:341 #EditStore: 342
        try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyCompanyModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroupModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("hierarchy_company"+storeHierarchyCompanyID+"Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeHierarchyCompanyModified)
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_id("hierarchy_storeGroup"+storeHierarchyStoreGroupID+"Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeHierarchyStoreGroupModified)
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_id("hierarchy_store"+storeHierarchyStoreID+"Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeHierarchyStoreModified)
        driver.find_element_by_id("renameOK").click()
        driver.refresh()
        for i in range(60):
            try:
                if storeHierarchyCompanyModified == driver.find_element_by_xpath("//li[@id='hierarchy_company"+storeHierarchyCompanyID+"']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(storeHierarchyCompany, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStore, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyCompanyModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroupModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        try: self.assertNotIn(storeHierarchyCompany, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStore, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyCompanyModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroupModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("hierarchy_company"+storeHierarchyCompanyID+"Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeHierarchyCompany)
        driver.find_element_by_id("renameOK").click()
       # driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_storeGroup"+storeHierarchyStoreGroupID+"Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeHierarchyStoreGroup)
        driver.find_element_by_id("renameOK").click()
        #driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_store"+storeHierarchyStoreID+"Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeHierarchyStore)
        driver.find_element_by_id("renameOK").click()
        #driver.find_element_by_css_selector("button.exit").click()
        driver.refresh()
        for i in range(60):
            try:
                if storeHierarchyCompany == driver.find_element_by_xpath("//li[@id='hierarchy_company"+storeHierarchyCompanyID+"']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyCompanyModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroupModified, driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreModified, driver.find_element_by_class_name("genericBrowser").text)
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
