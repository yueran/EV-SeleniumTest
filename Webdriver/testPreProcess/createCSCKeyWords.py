# To change this template, choose Tools | Templates
# and open the template in the editor.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_CreateGroups as CreateUserGroups

import unittest, time, re
from selenium.webdriver import ActionChains
#import HTMLTestRunner
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *

testUserId = None
testUserIdValue = None
testUserGroupId = None
testUserGroupIdValue = None

class createCSCKeywords(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_csc_keywords(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys(userName)
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys(userPassword)
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
        gb_frame(self)

        driver.get(self.base_url + "/ev/classifyproducts")

        driver.find_element_by_css_selector("span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys(classifyProductsCategory)
        driver.find_element_by_id("okCategory").click()
        driver.refresh()
        driver.find_element_by_css_selector("div.itemContent.subCategoryBg > span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys(classfiyProductsSubCategory)
        Select(driver.find_element_by_css_selector("select.CategoryMenu")).select_by_visible_text(classifyProductsCategory)
        driver.find_element_by_id("okSubcategory").click()
        driver.find_element_by_css_selector("div.itemContent.keywordBg > span.add").click()
        driver.find_element_by_css_selector("input.inputInfo").clear()
        driver.find_element_by_css_selector("input.inputInfo").send_keys(classifyProductsKeyword )
        Select(driver.find_element_by_css_selector("select.CategoryMenu")).select_by_visible_text(classifyProductsCategory)
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
        classifyProductsCategoryId = driver.find_element_by_xpath("//ul[@id='categoryBrowser']/li[1]").get_attribute("id")
#        print "classifyProductsCategoryId="+classifyProductsCategoryId
        classifyProductsCategoryIdValue = re.sub("\D","",classifyProductsCategoryId)
        print "classifyProductsCategoryIdValue=\""+classifyProductsCategoryIdValue+"\""
        driver.find_element_by_xpath("//li[@id='categoryCol_category"+classifyProductsCategoryIdValue+"']/div/span").click()
        #self.driver.implicitly_wait(30)
#False Negative, test it manually!!
        try: self.assertIn(classifyProductsCategory, driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(classfiyProductsSubCategory, driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(classifyProductsKeyword, driver.find_element_by_id("categoryBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print "Please record the ids for classifyProductsKeyword,classifyProductsCategory and classifyProductsSubCategory in ids.py"
#########################################################################################################################################3
        classifyProductsCategoryId = driver.find_element_by_xpath("//ul[@id='categoryBrowser']/li[1]").get_attribute("id")
#        print "classifyProductsCategoryId="+classifyProductsCategoryId
        classifyProductsCategoryIdValue = re.sub("\D","",classifyProductsCategoryId)
        print "classifyProductsCategoryIdValue=\""+classifyProductsCategoryIdValue+"\""

        classifyProductsSubCategoryId = driver.find_element_by_xpath("//ul[@id='categoryBrowser']/li[1]/ul[1]/li").get_attribute("id")
#        print "classifyProductsCategoryId="+classifyProductsCategoryId
        classifyProductsSubCategoryIdValue = re.sub("\D","",classifyProductsSubCategoryId)
        print "classifyProductsSubCategoryIdValue=\""+classifyProductsSubCategoryIdValue+"\""

        classifyProductsKeywordId = driver.find_element_by_xpath("//ul[@id='categoryBrowser']/li[1]/ul[2]/li").get_attribute("id")
#        print "classifyProductsKeywordId="+classifyProductsKeywordId
        classifyProductsKeywordIdValue = re.sub("\D","",classifyProductsKeywordId)
        print "classifyProductsKeywordIdValue=\""+classifyProductsKeywordIdValue+"\""
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
