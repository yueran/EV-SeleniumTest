from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *

class EnScheduleLoopsFunctionEditLoopSchedule1(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_loops_function_edit_loop_schedule1(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduleloop")
        try: self.assertIn(u"EditLoopSchedule", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule482 > div.itemContent.attractLoopBg > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule482 > div.itemContent.attractLoopBg > span.options.scheduleLoopOptions"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleCol_schedule482 > div.itemContent.attractLoopBg > span.fold").click()

        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule482 > div.scheduleInfo > span.dateSettings > label").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        
        try: self.assertIn("Start Date:", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"End Date:", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Start Time:", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"End Time:", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual("06/20/2012", driver.find_element_by_id("scheduleCol_schedule482startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("07/31/2012", driver.find_element_by_id("scheduleCol_schedule482endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("00:00:00", driver.find_element_by_id("scheduleCol_schedule482startTime").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("00:00:00", driver.find_element_by_id("scheduleCol_schedule482endTime").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CLASS_NAME,"timeEntry_control"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.ID,"schedule482allWeek"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Sun"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Mon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Tues"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Wed"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Thur"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Fri"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"schedule482Sat"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertIn(u"All Week", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Sun", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Mon", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Tues", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Wed", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Thur", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Fri", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Sat", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.XPATH,"//li[@id='scheduleCol_schedule482']/div[2]/span[2]/label[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_xpath("//li[@id='scheduleCol_schedule482']/div/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()