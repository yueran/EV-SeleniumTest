# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnTemplateStyleContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_template_style_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/templatestyles")
        try: self.assertTrue(self.is_element_present(By.ID, "pageTitle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Template Styles", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#welcomeTitle > span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header']/div[2]/div[2]/a/button"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader.templateBar"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Search Templates", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "templateSearch"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Select a Template", driver.find_element_by_id("selectTemplate").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.bigDownArrow").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.blockText.selectedText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.menu"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "title"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"No Template Loaded", driver.find_element_by_id("name").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "touch"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"1", driver.find_element_by_id("touch").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Nontouch", driver.find_element_by_xpath("//div[@id='title']/div[3]/label[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"0", driver.find_element_by_id("nontouch").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Basic", driver.find_element_by_id("basicTab").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Advanced", driver.find_element_by_id("advancedTab").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"New", driver.find_element_by_id("newTemplate").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "newTemplate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Save", driver.find_element_by_id("saveTemplate").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "saveTemplate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "duplicateTemplate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Duplicate", driver.find_element_by_id("duplicateTemplate").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "deleteTemplate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Delete", driver.find_element_by_id("deleteTemplate").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonLeft"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertIn(u"off", driver.find_element_by_id("buttonLeft").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Left\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonTop"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertIn(u"off", driver.find_element_by_id("buttonTop").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Top\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonBottom"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertIn(u"off", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Bottom\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonRight"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertIn("off", driver.find_element_by_id("buttonRight").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Right\"]"))
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
