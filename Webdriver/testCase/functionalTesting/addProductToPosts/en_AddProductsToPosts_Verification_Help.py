from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *

class EnAddProductsToPostsHelp(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_add_products_to_posts_help(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/addproductstoposts")
        driver.find_element_by_xpath("//div[@id='footer']/div").click()
        try: self.assertEqual("Help", driver.find_element_by_css_selector("span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(addProductsToPostsHelpLine1, driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(addProductsToPostsHelpLine2, driver.find_element_by_id("helpBody").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img.exit").click()
        driver.find_element_by_css_selector("span[title=\"Manage InStore Display\"]").click()
        driver.find_element_by_link_text("Add Posts to Display").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
