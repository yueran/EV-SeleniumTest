from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnViewNetworkStatusFunctionResetPwd(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_view_network_status_function_reset_pwd(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/viewnetworkstatus")
		try: self.assertEqual("Reset Password", driver.find_element_by_css_selector("span.resetPassword > button").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_css_selector("span.resetPassword > button").click()
		try: self.assertTrue(self.is_element_present(By.ID, "resetMediaPlayerPassword"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Reset Media Player Password", driver.find_element_by_css_selector("span").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Password:", driver.find_element_by_css_selector("span.name").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("", driver.find_element_by_id("passwordVal").get_attribute("value"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button.exit"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Cancel", driver.find_element_by_css_selector("button.exit").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Save", driver.find_element_by_id("resetMediaPlayerPassword").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("passwordVal").clear()
		driver.find_element_by_id("passwordVal").send_keys("testtest1")
		driver.find_element_by_id("resetMediaPlayerPassword").click()
		driver.find_element_by_css_selector("button.exit").click()
		driver.refresh()
		driver.find_element_by_css_selector("span.resetPassword > button").click()
		driver.find_element_by_id("passwordVal").clear()
		driver.find_element_by_id("passwordVal").send_keys("test")
		driver.find_element_by_id("resetMediaPlayerPassword").click()
		driver.find_element_by_css_selector("button.exit").click()
		# Negative Testing not be implemented yet.

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
