from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EnScheduleTemplatesFunctionEditTempSchedule2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.1.204:8080/"
        self.verificationErrors = []
    
    def test_en_schedule_templates_function_edit_temp_schedule2(self):
        driver = self.driver
        # Test Case not completed.
        try: self.assertEqual("03/01/2012", driver.find_element_by_id("scheduleCol_schedule193startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("5").click()
        try: self.assertEqual("03/05/2012", driver.find_element_by_id("scheduleCol_schedule193startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("03/30/2012", driver.find_element_by_id("scheduleCol_schedule193endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("25").click()
        try: self.assertEqual("03/25/2012", driver.find_element_by_id("scheduleCol_schedule193endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("00:00:00", driver.find_element_by_id("scheduleCol_schedule193startTime").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("23:00:00", driver.find_element_by_id("scheduleCol_schedule193endTime").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "scheduleCol_schedule193startTime"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule193startTime").click()
        # ERROR: Caught exception [ERROR: Unsupported command [typeKeys]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
