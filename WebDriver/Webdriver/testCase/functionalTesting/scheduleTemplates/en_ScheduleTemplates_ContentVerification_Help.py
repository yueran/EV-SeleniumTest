from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnScheduleTemplatesContentVerificationHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_templates_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduletemplates")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "title"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img.exit"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"First a template needs to have a schedule before it can be assigned to the Store Groups section. To schedule a template, click on the expander on the left side of the template tab. This will show start and end dates and times, along with days of the week.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"To assign a template to a Store group, Click and drag the template to the desired store group.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"A template can be assigned to any group.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.ID, "pop-up"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
