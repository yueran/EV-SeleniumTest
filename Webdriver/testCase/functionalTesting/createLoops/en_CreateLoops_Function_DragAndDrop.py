#drag and drop function testing is pending for the moment....
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnCreateLoopsFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_loops_function_drag_and_drop(self):
		driver = self.driver
		gb_login(self)
		driver.get(self.base_url + "/ev/createloops")
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='videoColumn_video"+video1ID+"']/div/div"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='aLCol_attractLoop"+assignLoopsID+"']/div/div"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		# ERROR: Caught exception [ERROR: Unsupported command [dragAndDropToObject]]
		try: self.assertEqual("", driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+assignLoopsID+"']/div/span").text)
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.refresh()
		driver.find_element_by_xpath("//li[@id='aLCol_attractLoop"+assignLoopsID+"']/div/span").click()
		driver.find_element_by_css_selector("span.unassign").click()
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
