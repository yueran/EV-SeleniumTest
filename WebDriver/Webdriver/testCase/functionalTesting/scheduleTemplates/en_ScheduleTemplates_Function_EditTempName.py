# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnScheduleTemplatesFunctionEditTempName(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_templates_function_edit_temp_name(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduletemplates")
        try: self.assertIn(u"ModifyTmp", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("scheduleCol_schedule462Options").click()
        driver.find_element_by_id("scheduleName").clear()
        driver.find_element_by_id("scheduleName").send_keys("SuccessModified")
        driver.find_element_by_id("scheduleOptionsPopup_OK").click()
        for i in range(60):
            try:
                if u"SuccessModified" == driver.find_element_by_css_selector("#scheduleCol_schedule462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"ModifyTmp", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.refresh()
        for i in range(60):
            try:
                if u"SuccessModified" == driver.find_element_by_css_selector("#scheduleCol_schedule462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"ModifyTmp", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule462Options").click()
        driver.find_element_by_id("scheduleName").clear()
        driver.find_element_by_id("scheduleName").send_keys("ModifyTmp")
        driver.find_element_by_id("scheduleOptionsPopup_OK").click()
        for i in range(60):
            try:
                if u"ModifyTmp" == driver.find_element_by_css_selector("#scheduleCol_schedule462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"ModifyTmp", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
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
