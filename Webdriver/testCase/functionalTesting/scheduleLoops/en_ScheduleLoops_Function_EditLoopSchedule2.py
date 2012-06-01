#Only start date, end date functions are tested. Functions for start time, end time, days of the week have not been tested yet.
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnScheduleLoopsFunctionEditLoopSchedule2(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
 #Note the test is time sensitive. Need to adjust the testing time as time goes by.
 #Test the start date and end date.
    def test_en_schedule_loops_function_edit_loop_schedule2(self):
        driver = self.driver
        gb_login(self)
        # Test Case not completed.
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduleloop")
        try: self.assertIn(EditLoopSchedule, driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule"+EditLoopScheduleID+"> div.itemContent.attractLoopBg > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule"+EditLoopScheduleID+" > div.itemContent.attractLoopBg > span.options.scheduleLoopOptions"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.itemContent.attractLoopBg > span.fold").click()

        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.scheduleInfo > span.dateSettings > label").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditLoopScheduleStartDate2, driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule"+EditLoopScheduleID+"startDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").click()
        driver.find_element_by_link_text(EditLoopScheduleStartDateKey1).click()
        for i in range(60):
            try:
                if EditLoopScheduleStartDate1 == driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditLoopScheduleStartDate1, driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
		
        driver.refresh()
        driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.itemContent.attractLoopBg > span.fold").click()
        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+"> div.scheduleInfo > span.dateSettings > label").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").click()
        driver.find_element_by_link_text(EditLoopScheduleStartDateKey2).click()
        for i in range(60):
            try:
                if EditLoopScheduleStartDate2 == driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditLoopScheduleStartDate2, driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual(EditLoopScheduleEndDate1, driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule"+EditLoopScheduleID+"endDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"endDate").click()
        driver.find_element_by_link_text(EditLoopScheduleEndDateKey1).click()
        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.scheduleInfo > span.dateSettings > label").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(EditLoopScheduleEndDate2, driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.refresh()
        driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.itemContent.attractLoopBg > span.fold").click()
        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.scheduleInfo > span.dateSettings > label").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"endDate").click()
        driver.find_element_by_link_text(EditLoopScheduleEndDateKey2).click()
        for i in range(60):
            try:
                if EditLoopScheduleEndDate1 == driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"endDate").get_attribute("value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")

        try: self.assertEqual(EditLoopScheduleEndDate1, driver.find_element_by_id("scheduleCol_schedule"+EditLoopScheduleID+"endDate").get_attribute("value"))
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
