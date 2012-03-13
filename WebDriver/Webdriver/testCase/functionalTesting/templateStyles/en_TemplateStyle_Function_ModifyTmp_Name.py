from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnTemplateStyleFunctionModifyTmpName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_template_style_function_modify_tmp_name(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/templatestyles")
        driver.find_element_by_css_selector("div.blockText.selectedText").click()
        driver.find_element_by_css_selector("div.menu").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_css_selector("div.blockText.selectedText").click()
        driver.find_element_by_css_selector("#templates_template462 > div.itemContent.templateBg > div.blockText").click()
        driver.find_element_by_css_selector("span.options").click()
        driver.find_element_by_id("newName").clear()
        driver.find_element_by_id("newName").send_keys("TmpNameIsChanged")
        driver.find_element_by_id("rename").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#renameTemplateOption > div.buttonStyle > button.exit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.refresh()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_css_selector("span.options").click()
        driver.find_element_by_id("newName").clear()
        driver.find_element_by_id("newName").send_keys("ModifyTmp")
        driver.find_element_by_id("rename").click()
        driver.find_element_by_css_selector("button.exit").click()
        driver.find_element_by_css_selector("#renameTemplateOption > div.buttonStyle > button.exit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.refresh()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
