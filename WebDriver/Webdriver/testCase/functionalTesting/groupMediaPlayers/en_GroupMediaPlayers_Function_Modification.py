from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnGroupMediaPlayersFunctionModification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_group_media_players_function_modification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/groupdevices")
        try: self.assertIn(u"test device 1 (store 15)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test device 1 (store 16)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"deviceModified", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("deviceCol_device27Options").click()
        driver.find_element_by_id("deviceName").clear()
        driver.find_element_by_id("deviceName").send_keys("deviceModified")
        driver.find_element_by_id("renameDevice").click()
        for i in range(60):
            try:
                if u"deviceModified" == driver.find_element_by_xpath("//li[@id='deviceCol_device27']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"test device 1 (store 15)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test device 1 (store 16)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"deviceModified", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        try: self.assertNotIn(u"test device 1 (store 15)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test device 1 (store 16)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"deviceModified", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("deviceCol_device27Options").click()
        driver.find_element_by_id("deviceName").clear()
        driver.find_element_by_id("deviceName").send_keys("test device 1 (store 15)")
        driver.find_element_by_id("renameDevice").click()

        driver.refresh()
        try: self.assertIn(u"test device 1 (store 15)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"test device 1 (store 16)", driver.find_element_by_class_name("deviceCol").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"deviceModified", driver.find_element_by_class_name("deviceCol").text)
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
