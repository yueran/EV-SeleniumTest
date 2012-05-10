from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *

class EnViewNetworkStatusContentVerificationHelp(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_view_network_status_content_verification_help(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/viewnetworkstatus")
		driver.find_element_by_xpath("//div[@id='footer']/div").click()
		try: self.assertEqual("Help", driver.find_element_by_id("title").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img.exit"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual(u"Help", driver.find_element_by_css_selector("span").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"This page displays the health of all media players. This includes:", driver.find_element_by_id("helpBody").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"DIB health", driver.find_element_by_id("helpBody").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"Active - Media player is communicating to the servers", driver.find_element_by_id("helpBody").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"Armed - All Secure display(s) is correctly connected", driver.find_element_by_id("helpBody").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"Media players can be searched through the heading or selected directly from the All Devices drop down menu.", driver.find_element_by_id("helpBody").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.ID, "pop-up"))
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
