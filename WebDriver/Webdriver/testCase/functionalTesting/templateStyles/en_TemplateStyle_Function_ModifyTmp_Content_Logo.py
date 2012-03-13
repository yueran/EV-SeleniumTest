from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnTemplateStyleFunctionModifyTmpContentLogo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_template_style_function_modify_tmp_content_logo(self):
        driver = self.driver
        # this one is pending.
        driver.get(self.base_url + "/ev/templatestyles")
        try: self.assertTrue(self.is_element_present(By.ID, "logo"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("width: 136.855px;", driver.find_element_by_id("log").get_attribute("id=logo"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("logo").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
