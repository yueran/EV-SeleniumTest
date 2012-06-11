from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnScheduleTemplatesFunctionSearch(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_schedule_templates_function_search(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/scheduletemplates")
		try: self.assertIn(EditTmpSchedule, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(templateStylesModifyTmp, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(templateStylesDuplicateTemp, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterTemplateText").clear()
		driver.find_element_by_id("filterTemplateText").send_keys(templateStylesModifyTmp)
		for i in range(60):
			try:
				if templateStylesModifyTmp == driver.find_element_by_css_selector("#scheduleCol_schedule"+templateStylesModifyTmpID+"> div.itemContent.templateBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertNotIn(EditTmpSchedule, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(templateStylesModifyTmp, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(templateStylesDuplicateTemp, driver.find_element_by_class_name("scheduleColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterTemplateText").clear()
		
		driver.refresh()
		try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(storeHierarchyStore, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		driver.find_element_by_id("filterStoreText").clear()
		driver.find_element_by_id("filterStoreText").send_keys(storeHierarchyCompany)
		for i in range(60):
			try:
				if templateStylesModifyTmp == driver.find_element_by_css_selector("#scheduleCol_schedule"+templateStylesModifyTmpID+"> div.itemContent.templateBg > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(storeHierarchyCompany, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(storeHierarchyStoreGroup, driver.find_element_by_class_name("storeHierarchyColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(storeHierarchyStore, driver.find_element_by_class_name("storeHierarchyColumn").text)
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
