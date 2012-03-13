from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *

class EnGroupMediaPlayersContentVerificationHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_group_media_players_content_verification_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/groupdevices")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertTrue(self.is_element_present(By.ID, "title"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Media Players can be assigned to only Stores and not Store Groups", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Devices and Store Groups sections can be sorted via a drop down or entering a name of the device or group.", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"Assign media players to groups by clicking and dragging from the Devices section to the store under the store groups section", driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img.exit"))
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
