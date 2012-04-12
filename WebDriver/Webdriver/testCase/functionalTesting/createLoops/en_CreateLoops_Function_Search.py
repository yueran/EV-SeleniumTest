from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnCreateLoopsFunctionSearch(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_create_loops_function_search(self):
		driver = self.driver
		# Manually test pass!
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_class_name("videoColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"John Denver Today.wmv", driver.find_element_by_class_name("videoColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterMediaText").clear()
		driver.find_element_by_id("filterMediaText").send_keys("MediaEditTest")
		for i in range(60):
			try:
				if u"MediaEditTest.avi" == driver.find_element_by_css_selector("#videoColumn_video184 > div.videoBg.itemContent > div.blockText").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_class_name("videoColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"John Denver Today.wmv", driver.find_element_by_class_name("videoColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterMediaText").clear()
		driver.find_element_by_id("filterMediaText").send_keys("")

		# AttractLoop
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"MediaEditTest.avi", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"ScheduleLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"testLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		Select(driver.find_element_by_id("filterLoopValue")).select_by_visible_text("Media")
		for i in range(60):
			try:
				if u"EditNameOfLoop" == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop478']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"ScheduleLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"testLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterMediaText").clear()
		driver.find_element_by_id("filterMediaText").send_keys("media")
		for i in range(60):
			try:
				if u"EditNameOfLoop" == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop478']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		self.driver.implicitly_wait(90)
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"ScheduleLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		#try: self.assertNotIn(u"testLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		#except AssertionError as e: self.verificationErrors.append(str(e))

		driver.refresh()
		#attract loops filter
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"MediaEditTest.avi", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"ScheduleLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"testLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		Select(driver.find_element_by_id("filterLoopValue")).select_by_visible_text("Attract Loops")
		for i in range(60):
			try:
				if u"EditNameOfLoop" == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop478']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"MediaEditTest.avi", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"ScheduleLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"testLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("filterLoopText").clear()
		driver.find_element_by_id("filterLoopText").send_keys("NameOfLoop")
		for i in range(60):
			try:
				if u"EditNameOfLoop" == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop478']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		self.driver.implicitly_wait(90)
		try: self.assertIn(u"EditNameOfLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"MediaEditTest.avi", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(u"ScheduleLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		#try: self.assertNotIn(u"testLoop", driver.find_element_by_class_name("attractLoopColumn").text)
		#except AssertionError as e: self.verificationErrors.append(str(e))

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
