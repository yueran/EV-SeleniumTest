#Drag and drop function testing is pending...
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnScheduleTemplatesFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_templates_function_drag_and_drop(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduletemplates")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
#        driver.find_element_by_xpath("//li[@id='hierarchy_storeGroup202']/div/span").click()
#        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#hierarchy_store203 > div.itemContent.storeBg > div.blockText"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#hierarchy_store"+groupMediaPlayersAssignStoreID+" > div.itemContent.storeBg > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#scheduleCol_schedule"+templateStylesDefaultTempID+" > div.itemContent.templateBg > div.handle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [dragAndDropToObject]]
        driver.find_element_by_xpath("//li[@id='hierarchy_store"+groupMediaPlayersAssignStoreID+"']/div/span").click()
        driver.refresh()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#scheduleContainersCol_container"+groupMediaPlayersAssignStoreID+" _schedule"+templateStylesDefaultTempID+" > div.itemContent.templateBg > span.unassign"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleContainersCol_container"+groupMediaPlayersAssignStoreID+" _schedule"+templateStylesDefaultTempID+"> div.itemContent.templateBg > span.unassign").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
