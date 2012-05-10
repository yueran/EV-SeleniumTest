from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *

class EnScheduleLoopsFunctionSearch(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_schedule_loops_function_search(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/scheduleloop")
		try: self.assertIn(u"EditLoopSchedule", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"test", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterSchedule").clear()
		driver.find_element_by_id("filterSchedule").send_keys("EditNameOfLoop")
		for i in range(60):
			try:
				if u"EditNameOfLoop" == driver.find_element_by_css_selector("#scheduleCol_schedule483 > div.itemContent.attractLoopBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertNotIn(u"EditLoopSchedule", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"test", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterSchedule").clear()
		
		driver.refresh()
		try: self.assertNotIn(u"EditLoopSchedule", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"EditStore", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"aaa", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterStore").clear()
		driver.find_element_by_id("filterStore").send_keys("edit")
		for i in range(60):
			try:
				if u"EditStore" == driver.find_element_by_css_selector("#hierarchy_store342 > div.itemContent.storeBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(u"EditLoopSchedule", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"EditStore", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"aaa", driver.find_element_by_class_name("storeHierarchyColumn").text)
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
