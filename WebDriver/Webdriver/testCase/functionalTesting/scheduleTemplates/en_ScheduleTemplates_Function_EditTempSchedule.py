from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnScheduleTemplatesFunctionEditTempSchedule1(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_templates_function_edit_temp_schedule1(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduletemplates")
        try: self.assertIn(u"EditTmpSchedule", driver.find_element_by_class_name("templateColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule918 > div.itemContent.templateBg > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule918Options"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleCol_schedule918 > div.itemContent.templateBg > span.fold").click()

        for i in range(60):
            try:
                if u"Start Date:" == driver.find_element_by_css_selector("#scheduleCol_schedule918 > div.scheduleInfo > span.dateSettings > label > span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        
        try: self.assertEqual("Start Date:", driver.find_element_by_css_selector("#scheduleCol_schedule918 > div.scheduleInfo > span.dateSettings > label > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"End Date:", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span/label[2]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Start Time:", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span/label[3]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"End Time:", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span/label[4]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule918startDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule918endDate"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule918startTime"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"scheduleCol_schedule918endTime"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("--/--/--", driver.find_element_by_id("scheduleCol_schedule918startDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("--/--/--", driver.find_element_by_id("scheduleCol_schedule918endDate").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("00:00:00", driver.find_element_by_id("scheduleCol_schedule918startTime").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("00:00:00", driver.find_element_by_id("scheduleCol_schedule918endTime").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CLASS_NAME,"timeEntry_control"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.ID,"template918allWeek"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Sun"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Mon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Tues"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Wed"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Thur"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Fri"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID,"template918Sat"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertEqual(u"All Week", driver.find_element_by_css_selector("#scheduleCol_schedule918 > div.scheduleInfo > span.weekFlags > label > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Sun", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Mon", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Tues", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Wed", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[5]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Thur", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[6]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Fri", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[7]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Sat", driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div[2]/span[2]/label[8]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR,"#scheduleCol_schedule886 > div.itemContent.templateBg > div.handle"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_xpath("//li[@id='scheduleCol_schedule918']/div/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
