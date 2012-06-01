from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnTemplateStyleFunctionCreateTemplates(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    # Delete CreateTmp before testing
    def test_en_template_style_function_create_templates(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/templatestyles")
        driver.find_element_by_class_name("bigDownArrow")
        try: self.assertNotIn(templateStylesCreateTemp, driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("newTemplate").click()
        try: self.assertEqual("Create New Template", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Name:", driver.find_element_by_css_selector("div.pop-up-body > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "templateEditName"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "touchPopup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("touchPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "nontouchPopup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("nontouchPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='pop-up']/div[2]/div/label[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonLeftPopup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonLeftPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Left\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonTopPopup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Top\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonBottomPopup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Bottom\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "buttonRightPopup"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonRightPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Right\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.exit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Cancel", driver.find_element_by_css_selector("button.exit").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "createTemplate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Save", driver.find_element_by_id("createTemplate").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img.exit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("templateEditName").clear()
        driver.find_element_by_id("templateEditName").send_keys("CreateTmp")
        driver.find_element_by_id("buttonLeftPopup").click()
        #try: self.assertEqual("on", driver.find_element_by_id("buttonLeftPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonRightPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonTopPopup").click()
        #try: self.assertEqual("off", driver.find_element_by_id("buttonLeftPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
       # except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
       # except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonRightPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonBottomPopup").click()
        #try: self.assertEqual("off", driver.find_element_by_id("buttonLeftPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonRightPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonRightPopup").click()
        #try: self.assertEqual("off", driver.find_element_by_id("buttonLeftPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("buttonRightPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("nontouchPopup").click()
        #try: self.assertEqual("off", driver.find_element_by_id("touchPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("nontouchPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Top\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Bottom\"]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonTopPopup").click()
        #try: self.assertEqual("on", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("off", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonBottomPopup").click()
        #try: self.assertEqual("off", driver.find_element_by_id("buttonTopPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("on", driver.find_element_by_id("buttonBottomPopup").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("touchPopup").click()
        driver.find_element_by_id("createTemplate").click()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
#reloading problem.
        for i in range(60):
            try:
                if templateStylesDefaultTemp == driver.find_element_by_css_selector("#templates_template"+templateStylesDefaultTempID +"> div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        try: self.assertIn(templateStylesCreateTemp, driver.find_element_by_id("templateSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        for i in range(60):
            try:
                if templateStylesDefaultTemp == driver.find_element_by_css_selector("#templates_template"+templateStylesDefaultTempID +"> div.itemContent.templateBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        
        try: self.assertIn(templateStylesCreateTemp, driver.find_element_by_id("templateSpace").text)
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
