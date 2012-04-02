from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnScheduleTemplatesFunctionSearch(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_schedule_templates_function_search(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/scheduletemplates")
		try: self.assertIn(u"EditTmpSchedule", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"ModifyTmp", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"DuplicateTmp", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterTemplateText").clear()
		driver.find_element_by_id("filterTemplateText").send_keys("ModifyTmp")
		for i in range(60):
			try:
				if u"ModifyTmp" == driver.find_element_by_css_selector("#scheduleCol_schedule462 > div.itemContent.templateBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertNotIn(u"EditTmpSchedule", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"ModifyTmp", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"DuplicateTmp", driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterTemplateText").clear()
		
		driver.refresh()
		try: self.assertIn(u"DuplicateStoreTest", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"EditStore", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterStoreText").clear()
		driver.find_element_by_id("filterStoreText").send_keys("edit")
		for i in range(60):
			try:
				if u"EditStore" == driver.find_element_by_css_selector("#hierarchy_store342 > div.itemContent.storeBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertNotIn(u"DuplicateStoreTest", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"EditStore", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"AssignMediaPlayer", driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterTemplateText").clear()

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
