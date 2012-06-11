#Only start date, end date functions are tested. Functions for start time, end time, days of the week have not been tested yet.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnScheduleTemplatesFunctionEditTempSchedule2(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
 #Note the test is time sensitive. Need to adjust the testing time as time goes by.
 #Test the start date and end date.
    def test_en_schedule_templates_function_edit_temp_schedule2(self):
        driver = self.driver
        gb_login(self)
        # Test Case not completed.
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduletemplates")
        try: self.assertIn(EditTmpSchedule, driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule"+EditTmpScheduleID+"> div.itemContent.templateBg > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule"+EditTmpScheduleID+"Options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleCol_schedule"+EditTmpScheduleID+" > div.itemContent.templateBg > span.fold").click()

        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditTmpScheduleID+"> div.scheduleInfo > span.dateSettings > label > span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditTmpScheduleStartDate2, driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule"+EditTmpScheduleID+"startDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").click()
#        driver.find_element_by_class_name("ui-datepicker-next").get_attribute("title")
        driver.find_element_by_link_text(EditTmpScheduleStartDateKey1).click()
        for i in range(60):
            try:
                if EditTmpScheduleStartDate1 == driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditTmpScheduleStartDate1, driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
		
        driver.refresh()
        driver.find_element_by_css_selector("#scheduleCol_schedule"+EditTmpScheduleID+"> div.itemContent.templateBg > span.fold").click()
        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditTmpScheduleID+"> div.scheduleInfo > span.dateSettings > label > span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").click()
        driver.find_element_by_link_text(EditTmpScheduleStartDateKey2 ).click()
        for i in range(60):
            try:
                if EditTmpScheduleStartDate2 == driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditTmpScheduleStartDate2, driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual(EditTmpScheduleEndDate1, driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule"+EditTmpScheduleID+"endDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").click()
        driver.find_element_by_link_text(EditTmpScheduleEndDateKey1).click()
        for i in range(60):
            try:
                if EditTmpScheduleEndDate2 == driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditTmpScheduleEndDate2, driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.refresh()
        driver.find_element_by_css_selector("#scheduleCol_schedule"+EditTmpScheduleID+"> div.itemContent.templateBg > span.fold").click()
        for i in range(60):
            try:
                if u"End Date:" == driver.find_element_by_xpath("//li[@id='scheduleCol_schedule"+EditTmpScheduleID+"']/div[2]/span/label[2]/span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").click()
        driver.find_element_by_link_text(EditTmpScheduleEndDateKey2).click()
        for i in range(60):
            try:
                if EditTmpScheduleEndDate1== driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        try: self.assertEqual(EditTmpScheduleEndDate1, driver.find_element_by_id("scheduleCol_schedule"+EditTmpScheduleID+"endDate").get_attribute("value"))
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
