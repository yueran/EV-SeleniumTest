from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnCreateLoopsContentVerificationHelp(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_create_loops_content_verification_help(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		driver.find_element_by_xpath("//div[@id='footer']/div").click()
		try: self.assertTrue(self.is_element_present(By.ID, "title"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("", driver.find_element_by_css_selector("img.exit").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"Multiple attract loops can be created in this section. To create an attract loop, click on the Create New Loop button. Name the attract loop, then begin adding Video media to the attract loop.", driver.find_element_by_id("helpBody").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(u"Video Media can be assigned to attract loops by clicking and dragging video media to an attract loop.", driver.find_element_by_id("helpBody").text)
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
