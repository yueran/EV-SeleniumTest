from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnTemplateStyleFunctionDuplicateTmp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
        # delete DuplicateCopyTmp before testing
    def test_en_template_style_function_duplicate_tmp(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/templatestyles")
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if templateStylesDuplicateTemp == driver.find_element_by_css_selector("#templates_template"+templateStylesDuplicateTempID+"> div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        #driver.find_element_by_css_selector("div.blockText.selectedText").click()
        try: self.assertIn(templateStylesDuplicateTemp, driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(templateStylesDuplicateTempCopy, driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#templates_template"+templateStylesDefaultTempID+"> div.itemContent.templateBg > div.blockText").click()

        driver.find_element_by_id("duplicateTemplate").click()
        driver.find_element_by_id("templateEditName").clear()
        driver.find_element_by_id("templateEditName").send_keys(templateStylesDuplicateTempCopy)
        driver.find_element_by_id("createTemplate").click()

        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.refresh()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if templateStylesDuplicateTemp == driver.find_element_by_css_selector("#templates_template"+templateStylesDuplicateTempID+"> div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(templateStylesDuplicateTemp, driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(templateStylesDuplicateTempCopy, driver.find_element_by_id("templateSpace").text)
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
