from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnCreateLoopsFunctionPreview(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_create_loops_function_preview(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		try: self.assertIn(editNameOfLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.play"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_css_selector("span.play").click()
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Video Preview", driver.find_element_by_css_selector("span").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("", driver.find_element_by_css_selector("img.exit").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.ID, "defaultPreviewVideo"))
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
