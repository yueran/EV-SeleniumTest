from selenium import webdriver
#Note: Need to delete 'NewAttractLoop' after testing...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnCreateLoopsFunctionCreateNewLoop(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_create_loops_function_create_new_loop(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		try: self.assertNotIn(NewAttractLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_css_selector("div.createNewLoop.commonButton").click()
		driver.find_element_by_id("loopName").clear()
		driver.find_element_by_id("loopName").send_keys("NewAttractLoop")
		driver.find_element_by_id("attractLoopPopupOK").click()
		for i in range(60):
			try:
				if assignLoops == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+assignLoopsIdValue+"']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(NewAttractLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.refresh()
		for i in range(60):
			try:
				if assignLoops == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+assignLoopsIdValue+"']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(NewAttractLoop, driver.find_element_by_class_name("attractLoopColumn").text)
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
