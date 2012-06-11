from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnViewNetworkStatusFunctionLockUnlock(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)

	def test_en_view_network_status_function_lock_unlock(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/viewnetworkstatus")
		try: self.assertTrue(self.is_element_present(By.ID, "lock_unlock_device"+Device1ID))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CLASS_NAME, "unlocked"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("lock_unlock_device"+Device1ID).click()
		try: self.assertTrue(self.is_element_present(By.ID, "lock_unlock_device"+Device1ID))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CLASS_NAME, "locked"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_id("lock_unlock_device"+Device1ID).click()
		try: self.assertTrue(self.is_element_present(By.CLASS_NAME, "locked"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.CLASS_NAME, "unlocked"))
		except AssertionError as e: self.verificationErrors.append(str(e))
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
