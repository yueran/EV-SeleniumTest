from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnStoreHierarchyContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_store_hierarchy_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/storehierarchy")
        gb_frame(self)
        try: self.assertEqual("Store Hierarchy", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Store Hierarchy", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Companies are structured in many different ways. Before setting-up user accounts and assign permissions to your team you will need to define your company's structure in relation to stores and devices within stores. Below is a sample default hierarchy. Delete the levels below or add new levels. Drag and drop the levels to change priority. Don't forget to save your company hierarchy. You can always change these settings later.", driver.find_element_by_id("body").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Start the process by reviewing and editing the example below.", driver.find_element_by_id("body").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "newCompany"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("New Company", driver.find_element_by_id("newCompany").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "newStoreGroup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("New Store Group", driver.find_element_by_id("newStoreGroup").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "newStore"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("New Store", driver.find_element_by_id("newStore").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.createNew.adder").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mediaScroll"))
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='hierarchy_company340']/div/div[2]"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.ID, "hierarchy_company340Options"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.handle"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.ID, "hierarchy_company340Duplicate"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.ID, "hierarchy_company340Remove"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
