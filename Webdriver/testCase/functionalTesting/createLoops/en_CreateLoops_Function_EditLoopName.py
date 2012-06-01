from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnCreateLoopsFunctionEditLoopNameAndCreateLoops(unittest.TestCase):
	def setUp(self):
		gb_setUp(self)
    
	def test_en_create_loops_function_edit_loop_name_and_create_loops(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		try: self.assertNotIn(NewAttractLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(EditNameOfLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertNotIn(EditLoopNameSuccess, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		#Create Loops:
		driver.find_element_by_css_selector("div.createNewLoop.commonButton").click()
		driver.find_element_by_id("loopName").clear()
		driver.find_element_by_id("loopName").send_keys(NewAttractLoop)
		driver.find_element_by_id("attractLoopPopupOK").click()

		#Edit Loop Name:
		driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+EditAttractLoopID+"']/div/span[3]").click()
		driver.find_element_by_id("loopName").clear()
		driver.find_element_by_id("loopName").send_keys(EditLoopNameSuccess)
		driver.find_element_by_id("attractLoopPopupOK").click()
		for i in range(60):
			try:
				if EditLoopNameSuccess == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+EditAttractLoopID+"']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")

#		#Verify Create Loops:
		try: self.assertIn(NewAttractLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))

		#Verify Edit Loop Name:
		try: self.assertNotIn(EditNameOfLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(EditLoopNameSuccess, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.refresh()
#		#Verify Create Loops:
		try: self.assertIn(NewAttractLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		#Verify Edit Loop Name:
		try: self.assertNotIn(EditNameOfLoop, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertIn(EditLoopNameSuccess, driver.find_element_by_class_name("attractLoopColumn").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.refresh()
		driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+EditAttractLoopID+"']/div/span[3]").click()
		driver.find_element_by_id("loopName").clear()
		driver.find_element_by_id("loopName").send_keys(EditNameOfLoop)
		driver.find_element_by_id("attractLoopPopupOK").click()
		for i in range(60):
			try:
				if EditNameOfLoop == driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+EditAttractLoopID+"']/div/div").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
        	try: self.assertIn(EditNameOfLoop, driver.find_element_by_class_name("attractLoopColumn").text)
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
