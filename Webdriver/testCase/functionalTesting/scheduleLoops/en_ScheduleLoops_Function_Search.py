from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnScheduleLoopsFunctionSearch(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_schedule_loops_function_search(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/scheduleloop")
		try: self.assertIn(EditLoopSchedule, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(EditNameOfLoop, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(DefaultAttractLoop, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterSchedule").clear()
		driver.find_element_by_id("filterSchedule").send_keys(EditLoopSchedule)
		for i in range(60):
			try:
				if EditLoopSchedule == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.itemContent.attractLoopBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(EditLoopSchedule, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(EditNameOfLoop, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(DefaultAttractLoop, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterSchedule").clear()
		
		driver.refresh()
		try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterStore").clear()
		driver.find_element_by_id("filterStore").send_keys(storeHierarchyCompany)
		for i in range(60):
			try:
				if EditLoopSchedule == driver.find_element_by_css_selector("#scheduleCol_schedule"+EditLoopScheduleID+" > div.itemContent.attractLoopBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(storeHierarchyStore, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterStore").clear()

		driver.refresh()
		
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True
		
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
