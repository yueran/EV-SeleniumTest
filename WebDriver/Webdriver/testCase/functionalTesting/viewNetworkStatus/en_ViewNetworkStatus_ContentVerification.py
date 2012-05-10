from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *

class EnViewNetworkStatusContentVerification(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_view_network_status_content_verification(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/viewnetworkstatus")
		gb_frame(self)
		try: self.assertTrue(self.is_element_present(By.ID, "pageTitle"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("View Network Status", driver.find_element_by_id("pageTitle").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Search", driver.find_element_by_css_selector("span.columnHeaderText").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		try: self.assertIn("All Devices", driver.find_element_by_id("selectedFilterValue").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn("Active", driver.find_element_by_id("selectedFilterValue").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn("Inactive", driver.find_element_by_id("selectedFilterValue").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn("Defective", driver.find_element_by_id("selectedFilterValue").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		try: self.assertTrue(self.is_element_present(By.ID, "filterText"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.blockText.selectedText"))
		except AssertionError as e: self.verificationErrors.append(str(e))

		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.bigDownArrow"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.deviceBg.itemContent > span.fold"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.play.inactive"))
		except AssertionError as e: self.verificationErrors.append(str(e))

		try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='devices_device27']/div/span[5]/span/span"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.resetPassword > button"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Reset Password", driver.find_element_by_css_selector("span.resetPassword > button").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.ID, "lock_unlock_device27"))
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
