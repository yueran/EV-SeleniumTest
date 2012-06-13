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
#        driver.find_element_by_xpath("//li[@id='categoryCol_category"+classifyProductsNewCategoryIdValue+"']/div/span").click()
#        try: self.assertNotIn("0NewCat", driver.find_element_by_id("categoryBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertNotIn("0newSubCat", driver.find_element_by_id("categoryBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertNotIn("0NewKey", driver.find_element_by_id("categoryBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("0NewCat")
        driver.find_element_by_id("okCategory").click()
        driver.find_element_by_css_selector("div.itemContent.subCategoryBg > span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("0newSubCat")
        Select(driver.find_element_by_css_selector("select.CategoryMenu")).select_by_visible_text(classifyProductsNewCategory)
        driver.find_element_by_id("okSubcategory").click()
        driver.find_element_by_css_selector("div.itemContent.keywordBg > span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys("0NewKey")
        Select(driver.find_element_by_css_selector("select.CategoryMenu")).select_by_visible_text(classifyProductsNewCategory)
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
        self.driver.implicitly_wait(30)
        driver.find_element_by_xpath("//li[@id='categoryCol_category"+classifyProductsNewCategoryIdValue+"']/div/span").click()
        #self.driver.implicitly_wait(30)
#False Negative, test it manually!!
        try: self.assertIn("0NewCat", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("0newSubCat", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("0NewKey", driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        self.driver.implicitly_wait(30)
        newCatId = driver.find_element_by_xpath("//ul[@id='categoryBrowser']/li[1]").get_attribute("id")
        newSubCatId = driver.find_element_by_xpath("//li[@id='categoryCol_category"+classifyProductsNewCategoryIdValue+"']/ul[1]/li[1]").get_attribute("id")
        newKeywordId = driver.find_element_by_xpath("//li[@id='categoryCol_category"+classifyProductsNewCategoryIdValue+"']/ul[2]/li[1]").get_attribute("id")
        newCatIdValue = re.sub("\D","",newCatId)
        newSubCatIdValue = re.sub("\D","",newSubCatId)
        newKeywordIdValue = re.sub("\D","",newKeywordId)
        print "newCatIdValue=\""+newCatIdValue+"\"\n"
        print "newSubCatIdValue=\""+newSubCatIdValue+"\"\n"
        print "newKeywordIdValue=\""+newKeywordIdValue+"\"\n"

        text_file = open(gb_Preprocess_ids_Prefix + "ids.py", "a")
    #        ids =[]
        text_file.write("#**********************************************\n")
        text_file.write("newCatIdValue=\""+newCatIdValue+"\"\n")
        text_file.write("newSubCatIdValue=\""+newSubCatIdValue+"\"\n")
        text_file.write("newKeywordIdValue=\""+newKeywordIdValue+"\"\n")
    #        text_file.write(("".join(ids))+"\n")
        text_file.close()
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
