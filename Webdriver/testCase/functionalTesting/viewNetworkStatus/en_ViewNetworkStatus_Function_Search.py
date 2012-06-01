from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnViewNetworkStatusFunctionSearch(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_view_network_status_function_search(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/viewnetworkstatus")
		#Search by category
		try: self.assertIn(Device1, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(Device2, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("Active")
		try: self.assertIn(Device1, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(Device2, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("Inactive")
		try: self.assertNotIn(Device1, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(Device2, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("Defective")
		try: self.assertNotIn(Device1, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(Device2, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("All Devices")
		try: self.assertIn(Device1, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(Device2, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		# Search by specific Keyword:
		driver.find_element_by_id("filterText").send_keys("15")
		try: self.assertIn(Device1, driver.find_element_by_class_name("mainContentDiv").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(Device2, driver.find_element_by_class_name("mainContentDiv").text)
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
