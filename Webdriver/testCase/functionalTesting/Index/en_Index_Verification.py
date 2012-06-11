from selenium.common.exceptions import NoSuchElementException
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnIndexVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_index_verification(self):
        driver = self.driver
        gb_login(self)
        gb_frame(self)
        try: self.assertEqual("Welcome", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("img[alt=\"welcome image\"]").text)
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
