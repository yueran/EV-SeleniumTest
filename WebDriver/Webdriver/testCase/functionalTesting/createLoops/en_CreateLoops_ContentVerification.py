from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *

class EnCreateLoopsContentVerification(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)
    
	def test_en_create_loops_content_verification(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		gb_frame(self)
		try: self.assertTrue(self.is_element_present(By.ID, "pageTitle"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Create Loops", driver.find_element_by_id("pageTitle").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.columnHeader"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Video Media", driver.find_element_by_css_selector("span.columnHeaderText").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.ID, "filterMediaText"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.searchIcon"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Upload New Video", driver.find_element_by_xpath("//div[@id='body']/div[2]/div/div[2]/div").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='body']/div[2]/div/div[2]/div"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='body']/div[2]/div/div[2]/span"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.blockText"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("", driver.find_element_by_css_selector("span.play").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.ID, "video_videoDelete205"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.attractLoopColumn > div.columnHeader > span.columnHeaderText"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.attractLoopColumn > div.columnHeader > span.columnHeaderText"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn("Media", driver.find_element_by_id("filterLoopValue").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn("Attract Loops", driver.find_element_by_id("filterLoopValue").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.ID, "filterLoopText"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.attractLoopColumn > div.columnHeader > span.searchIcon"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.createNewLoop.commonButton"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertEqual("Create New Loop", driver.find_element_by_css_selector("div.createNewLoop.commonButton").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.newLoopButton.adder"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.newLoopButton.adder"))
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
