#This one is pending....
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnGroupMediaPlayersFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_group_media_players_function_drag_and_drop(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/groupdevices")
        Select(driver.find_element_by_id("filterStoresBy")).select_by_visible_text("")
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='deviceCol_device"+groupMediaPlayersDeviceStore15ID+"']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//li[@id='hierarchy_store"+groupMediaPlayersAssignStoreID+"']/div/span").click()
#        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#hierarchy_store200 > div.itemContent.storeBg > div.blockText"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [dragAndDropToObject]]
        driver.find_element_by_xpath("//li[@id='hierarchy_store200']/div/span").click()
        driver.find_element_by_id("deviceContainersCol_device28Unassign").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
