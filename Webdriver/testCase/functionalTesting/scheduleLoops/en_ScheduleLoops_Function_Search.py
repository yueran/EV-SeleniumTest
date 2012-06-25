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
		try: self.assertIn(editLoopSchedule, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(editNameOfLoop, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(assignLoops, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterSchedule").clear()
		driver.find_element_by_id("filterSchedule").send_keys(editLoopSchedule)
		for i in range(60):
			try:
				if editLoopSchedule == driver.find_element_by_css_selector("#scheduleCol_schedule"+editLoopScheduleIdValue+" > div.itemContent.attractLoopBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(editLoopSchedule, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(editNameOfLoop, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(assignLoops, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterSchedule").clear()
		
		driver.refresh()
		try: self.assertIn(companyTest, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(storeGroupTest, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(storeTest, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterStore").clear()
		driver.find_element_by_id("filterStore").send_keys(companyTest)
		for i in range(60):
			try:
				if companyTest == driver.find_element_by_css_selector("#hierarchy_company"+companyTestIdValue+" > div.itemContent.companyBg > div.blockText").text: break
			except: pass
#			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(companyTest, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(storeGroupTest, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(storeTest, driver.find_element_by_class_name("storeHierarchyColumn").text)
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
