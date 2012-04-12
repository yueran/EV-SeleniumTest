from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnCreateLoopsFunctionUploadNewVideo(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_create_loops_function_upload_new_video(self):
		driver = self.driver
		gb_login(self)
		# Uploading function could not be tested for the moment.
		driver.get(self.base_url + "/ev/createloops")
		driver.find_element_by_xpath("//div[@id='body']/div[2]/div/div[2]/div").click()
		try: self.assertEqual("Upload Video", driver.find_element_by_css_selector("span").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.NAME, "file"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("", driver.find_element_by_name("file").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.exit.buttonStyle"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_css_selector("img.exit").click()

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
