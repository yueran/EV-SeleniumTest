# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *

class EnScheduleLoopsFunctionEditLoopName(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_loops_function_edit_loop_name(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduleloop")
        try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_css_selector("#scheduleCol_schedule483 > div.itemContent.attractLoopBg > span.options.scheduleLoopOptions").click()
        driver.find_element_by_id("scheduleName").clear()
        driver.find_element_by_id("scheduleName").send_keys("SuccessModified")
        driver.find_element_by_id("scheduleOptionsPopup_OK").click()
        for i in range(60):
            try:
                if u"SuccessModified" == driver.find_element_by_css_selector("#scheduleCol_schedule483 > div.itemContent.attractLoopBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"EditNameOfLoop", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.refresh()
        for i in range(60):
            try:
                if u"SuccessModified" == driver.find_element_by_css_selector("#scheduleCol_schedule483 > div.itemContent.attractLoopBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"EditNameOfLoop", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("#scheduleCol_schedule483 > div.itemContent.attractLoopBg > span.options.scheduleLoopOptions").click()
        driver.find_element_by_id("scheduleName").clear()
        driver.find_element_by_id("scheduleName").send_keys("EditNameOfLoop")
        driver.find_element_by_id("scheduleOptionsPopup_OK").click()
        for i in range(60):
            try:
                if u"EditNameOfLoop" == driver.find_element_by_css_selector("#scheduleCol_schedule483 > div.itemContent.attractLoopBg > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"SuccessModified", driver.find_element_by_class_name("scheduleColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
