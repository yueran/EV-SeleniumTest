from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnTemplateStyleFunctionModifyTmpContentTouchNontouch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_template_style_function_modify_tmp_content_touch_nontouch(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/templatestyles")
        driver.find_element_by_css_selector("div.blockText.selectedText").click()
        driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").click()
        try: self.assertEqual("on", driver.find_element_by_id("touch").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.touchNavButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.touchButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='touchButtons']/div[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='touchButtons']/div[3]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='touchButtons']/div[4]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='touchButtons']/div[5]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.touchNavButton.navigationRight"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("buttonTop").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonLeft").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonRight").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonLeft").click()
        try: self.assertEqual("on", driver.find_element_by_id("buttonLeft").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonTop").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonRight").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonBottom").click()
        try: self.assertEqual("on", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonLeft").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonTop").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonRight").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonRight").click()
        try: self.assertEqual("off", driver.find_element_by_id("buttonLeft").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonTop").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("buttonRight").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonTop").click()
        driver.find_element_by_id("nontouch").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.nontouchButtonImgBox"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='nontouchButtons']/div[2]/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='nontouchButtons']/div[3]/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("buttonTop").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("off", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("buttonBottom").click()
        try: self.assertEqual("off", driver.find_element_by_id("buttonTop").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("on", driver.find_element_by_id("buttonBottom").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("touch").click()
        driver.find_element_by_id("buttonTop").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
