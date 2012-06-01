#Drag and drop function testing is pending...
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnScheduleLoopsFunctionDragAndDrop(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_schedule_loops_function_drag_and_drop(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/scheduleloop")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
#this test case is pending...for the moment...
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
