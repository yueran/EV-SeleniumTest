from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnGroupMediaPlayersContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_group_media_players_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/groupdevices")
        gb_frame(self)
        try: self.assertTrue(self.is_element_present(By.ID, "pageTitle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Group Media Players", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Media Players", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterDevicesText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.storeGroupCol > div.columnHeader > span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Store Hierarchy", driver.find_element_by_css_selector("div.storeGroupCol > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Active", driver.find_element_by_id("filterDevicesBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("InActive", driver.find_element_by_id("filterDevicesBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Error", driver.find_element_by_id("filterDevicesBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Assigned", driver.find_element_by_id("filterDevicesBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Unassigned", driver.find_element_by_id("filterDevicesBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Device", driver.find_element_by_id("filterStoresBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Store", driver.find_element_by_id("filterStoresBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Store Group", driver.find_element_by_id("filterStoresBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Company", driver.find_element_by_id("filterStoresBy").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterStoreText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.storeGroupCol > div.columnHeader > span.searchArea > span.searchBody > span.searchIcon"))
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
