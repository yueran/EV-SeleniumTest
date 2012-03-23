from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnScheduleTemplatesFunctionEditTempSchedule2(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
 #Note the test is time sensitive. Need to adjust the testing time as time goes by.
    def test_en_schedule_templates_function_edit_temp_schedule2(self):
        driver = self.driver
        gb_login(self)
        # Test Case not completed.
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduletemplates")
        try: self.assertIn(u"EditTempSchedule2", driver.find_element_by_class_name("templateColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule919 > div.itemContent.templateBg > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule919Options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleCol_schedule919 > div.itemContent.templateBg > span.fold").click()

        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule919 > div.scheduleInfo > span.dateSettings > label > span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("04/01/2012", driver.find_element_by_id("scheduleCol_schedule919startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule919startDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule919startDate").click()
        driver.find_element_by_link_text("5").click()
        for i in range(60):
            try:
                if u"04/05/2012" == driver.find_element_by_id("scheduleCol_schedule919startDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("04/05/2012", driver.find_element_by_id("scheduleCol_schedule919startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule919startDate").click()
        driver.find_element_by_link_text("1").click()
        for i in range(60):
            try:
                if u"04/01/2012" == driver.find_element_by_id("scheduleCol_schedule919startDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("04/01/2012", driver.find_element_by_id("scheduleCol_schedule919startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual("07/31/2012", driver.find_element_by_id("scheduleCol_schedule919endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule919endDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule919endDate").click()
        driver.find_element_by_link_text("25").click()
        for i in range(60):
            try:
                if u"07/25/2012" == driver.find_element_by_id("scheduleCol_schedule919endDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("07/25/2012", driver.find_element_by_id("scheduleCol_schedule919endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule919endDate").click()
        driver.find_element_by_link_text("31").click()
        for i in range(60):
            try:
                if u"07/31/2012" == driver.find_element_by_id("scheduleCol_schedule919endDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("07/31/2012", driver.find_element_by_id("scheduleCol_schedule919endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))


        #try: self.assertEqual("00:00:00", driver.find_element_by_id("scheduleCol_schedule919startTime").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #try: self.assertEqual("23:00:00", driver.find_element_by_id("scheduleCol_schedule919endTime").get_attribute("value"))
        #except AssertionError as e: self.verificationErrors.append(str(e))

        #driver.find_element_by_id("scheduleCol_schedule919startTime").click()
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
