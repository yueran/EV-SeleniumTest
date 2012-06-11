from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnCreateLoopsFunctionSequenceNo(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_loops_function_sequence_no(self):
        driver = self.driver
		
        # This one is not implemented for the moment.
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
