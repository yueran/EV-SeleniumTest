#Notes: need to remove the newly created Category/Subcategory/keyword manually at the end of the testing.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
class EnClassifyProductsFunctionAddElement(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_classify_products_function_add_element(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/classifyproducts")
#Verify if the Category, Subcategory and keyword successfully created by checking the name.
        driver.find_element_by_xpath("//li[@id='"+classifyProductsCategoryId+"']/div/span").click()
        try: self.assertNotIn("NewCat", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("newSubCat", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("NewKey", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("NewCat")
        driver.find_element_by_id("okCategory").click()
        driver.find_element_by_css_selector("div.itemContent.subCategoryBg > span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("newSubCat")
        Select(driver.find_element_by_css_selector("select.CategoryMenu")).select_by_visible_text("test")
        driver.find_element_by_id("okSubcategory").click()
        driver.find_element_by_css_selector("div.itemContent.keywordBg > span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("NewKey")
        Select(driver.find_element_by_css_selector("select.CategoryMenu")).select_by_visible_text("test")
        #Select(driver.find_element_by_css_selector("select.SubcategoryMenu")).select_by_visible_text("AddElementsSub")
        driver.find_element_by_id("rangeKeywordLowerValue").clear()
        driver.find_element_by_id("rangeKeywordLowerValue").send_keys("1")
        driver.find_element_by_id("rangeKeywordUpperValue").clear()
        driver.find_element_by_id("rangeKeywordUpperValue").send_keys("2")
        driver.find_element_by_id("okAddKeywordValue").click()
        driver.find_element_by_id("okKeyword").click()

#Verify if the Category, Subcategory and keyword successfully created by checking the name.
        self.driver.implicitly_wait(30)
        driver.refresh()
        driver.find_element_by_xpath("//li[@id='"+classifyProductsCategoryId+"']/div/span").click()
        #self.driver.implicitly_wait(30)
#False Negative, test it manually!!
        try: self.assertIn("NewCat", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("newSubCat", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("NewKey", driver.find_element_by_id("categoryBrowser").text)
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
