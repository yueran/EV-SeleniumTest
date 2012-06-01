from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#from configglue.inischema.attributed import value
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnGroupMediaPlayersFunctionSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_group_media_players_function_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/groupdevices")
        try: self.assertIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("filterDevicesBy")).select_by_visible_text("Active")
        try: self.assertIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("filterDevicesBy")).select_by_visible_text("InActive")
        try: self.assertNotIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("filterDevicesBy")).select_by_visible_text("Error")
        try: self.assertNotIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("filterDevicesBy")).select_by_visible_text("Assigned")
        try: self.assertIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("filterDevicesBy")).select_by_visible_text("Unassigned")
        try: self.assertNotIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("filterDevicesBy")).select_by_visible_text("")
        try: self.assertIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterDevicesText").clear()
        driver.find_element_by_id("filterDevicesText").send_keys("15")
        driver.find_element_by_css_selector("span.searchIcon").click()
        try: self.assertIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterDevicesText").clear()
#**************************************************************************************************************************
        # Store Hierarchy search
        driver.find_element_by_id("filterStoreText").clear()
        driver.find_element_by_id("filterStoreText").send_keys("a")
        try: self.assertTrue(self.is_element_present(By.ID, "popup_container"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Alert", driver.find_element_by_id("popup_title").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Please select type to filter by", driver.find_element_by_id("popup_message").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertIn(u"OK", driver.find_element_by_id("popup_container").text)
        #except AssertionError as e: self.verificationErrors.append(str(e))
        self.driver.implicitly_wait(60)
        driver.find_element_by_id("popup_ok").click()
#        try: self.assertIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeGroupCol").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #device:
        Select(driver.find_element_by_id("filterStoresBy")).select_by_visible_text("Device")
#        try: self.assertIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeGroupCol").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(groupMediaPlayersDeviceStore15, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyCompany, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #Store:
        Select(driver.find_element_by_id("filterStoresBy")).select_by_visible_text("Store")
#        try: self.assertIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeGroupCol").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyCompany, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #Store Group:
        Select(driver.find_element_by_id("filterStoresBy")).select_by_visible_text("Store Group")
#        try: self.assertNotIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeGroupCol").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyCompany, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStore, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        #Company:
        Select(driver.find_element_by_id("filterStoresBy")).select_by_visible_text("Company")
#        try: self.assertNotIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeGroupCol").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(groupMediaPlayersDeviceStore16, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStore, driver.find_element_by_class_name("storeGroupCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeGroupCol").text)
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
