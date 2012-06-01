from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnScheduleLoopsContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_loops_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduleloop")
        gb_frame(self)
        try: self.assertTrue(self.is_element_present(By.ID, "pageTitle"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Schedule Loop", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Attract Loops", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterSchedule"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#scheduleCol_schedule483 > div.itemContent.attractLoopBg > span.options.scheduleLoopOptions"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#scheduleCol_schedule483 > div.itemContent.attractLoopBg > span.fold"))
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.storeHierarchyColumn > div.columnHeader"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Store Hierarchy", driver.find_element_by_css_selector("div.storeHierarchyColumn > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "filterStore"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.storeHierarchyColumn > div.columnHeader > span.searchIcon"))
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
