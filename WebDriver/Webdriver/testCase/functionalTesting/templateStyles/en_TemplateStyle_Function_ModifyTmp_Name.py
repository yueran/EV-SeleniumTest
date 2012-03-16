from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnTemplateStyleFunctionModifyTmpName(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_template_style_function_modify_tmp_name(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/templatestyles")
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if u"ModifyTmp" == driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"ModifyTmp", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"TmpNameIsChanged", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").click()
        driver.find_element_by_css_selector("span.options").click()
        driver.find_element_by_id("newName").clear()
        driver.find_element_by_id("newName").send_keys("TmpNameIsChanged")
        driver.find_element_by_id("rename").click()

        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if u"TmpNameIsChanged" == driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"ModifyTmp", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"TmpNameIsChanged", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if u"TmpNameIsChanged" == driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"ModifyTmp", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"TmpNameIsChanged", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_css_selector("span.options").click()
        driver.find_element_by_id("newName").clear()
        driver.find_element_by_id("newName").send_keys("ModifyTmp")
        driver.find_element_by_id("rename").click()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if u"ModifyTmp" == driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"ModifyTmp", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"TmpNameIsChanged", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if u"ModifyTmp" == driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"ModifyTmp", driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"TmpNameIsChanged", driver.find_element_by_id("templateSpace").text)
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
