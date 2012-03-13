from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnStoreHierarchyFunctionModification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_store_hierarchy_function_modification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/storehierarchy")
        #id:EditCompany: 340 #EditStoreGroup:341 #EditStore: 342
        try: self.assertIn(u"EditCompany", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"EditStoreGroup", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"EditStore", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"CompanyModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"StoreGroupModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"StoreModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("hierarchy_company340Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("CompanyModified")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_id("hierarchy_storeGroup341Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("StoreGroupModified")
        driver.find_element_by_id("renameOK").click()
        driver.find_element_by_id("hierarchy_store342Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("StoreModified")
        driver.find_element_by_id("renameOK").click()
        driver.refresh
        for i in range(60):
            try:
                if u"CompanyModified" == driver.find_element_by_xpath("//li[@id='hierarchy_company340']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"EditCompany", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"EditStoreGroup", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"EditStore", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"CompanyModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"StoreGroupModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"StoreModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        try: self.assertNotIn(u"EditCompany", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"EditStoreGroup", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"EditStore", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"CompanyModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"StoreGroupModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"StoreModified", driver.find_element_by_class_name("genericBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("hierarchy_company340Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("EditCompany")
        driver.find_element_by_id("renameOK").click()
       # driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_storeGroup341Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("EditStoreGroup")
        driver.find_element_by_id("renameOK").click()
        #driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_id("hierarchy_store342Options").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys("EditStore")
        driver.find_element_by_id("renameOK").click()
        #driver.find_element_by_css_selector("button.exit").click()
        driver.refresh

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
