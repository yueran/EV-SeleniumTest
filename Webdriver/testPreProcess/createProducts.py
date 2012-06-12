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
from Webdriver.testPreProcess.input import *

testUserId = None
testUserIdValue = None
testUserGroupId = None
testUserGroupIdValue = None

class createProducts(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_products(self):
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

        driver.get(self.base_url + "/ev/createproducts")
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("--New Manufacturer--")
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys("test")
        driver.find_element_by_id("newManufacturer").click()
        driver.refresh()
        driver.get(self.base_url + "/ev/createproducts")
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("--New Manufacturer--")
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys("ManTest")
        driver.find_element_by_id("newManufacturer").click()
        driver.refresh()
        driver.find_element_by_id("newProduct").click()
        driver.find_element_by_id("product").click()
        try: self.assertIn("New Product", driver.find_element_by_id("productName").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("test")
        #Select(driver.find_element_by_id("detailCategory")).select_by_visible_text("")
        driver.find_element_by_id("detailModel").clear()
        driver.find_element_by_id("detailModel").send_keys(testProduct1)
        driver.find_element_by_id("detailSeries").clear()
        driver.find_element_by_id("saveProduct").click()

        driver.refresh()
        driver.find_element_by_id("newProduct").click()
        driver.find_element_by_id("product").click()
        try: self.assertIn("New Product", driver.find_element_by_id("productName").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("test")
        #Select(driver.find_element_by_id("detailCategory")).select_by_visible_text("")
        driver.find_element_by_id("detailModel").clear()
        driver.find_element_by_id("detailModel").send_keys(testProduct2)
        driver.find_element_by_id("detailSeries").clear()
        driver.find_element_by_id("saveProduct").click()

        driver.refresh()
        driver.find_element_by_id("newProduct").click()
        driver.find_element_by_id("accessory").click()
        try: self.assertIn("New Product", driver.find_element_by_id("productName").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("test")
        #Select(driver.find_element_by_id("detailCategory")).select_by_visible_text("")
        driver.find_element_by_id("detailModel").clear()
        driver.find_element_by_id("detailModel").send_keys(testAcc1)
        driver.find_element_by_id("detailSeries").clear()
        driver.find_element_by_id("saveProduct").click()

        driver.refresh()
        driver.find_element_by_id("newProduct").click()
        driver.find_element_by_id("accessory").click()
        try: self.assertIn("New Product", driver.find_element_by_id("productName").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("test")
        #Select(driver.find_element_by_id("detailCategory")).select_by_visible_text("")
        driver.find_element_by_id("detailModel").clear()
        driver.find_element_by_id("detailModel").send_keys(testAcc2)
        driver.find_element_by_id("detailSeries").clear()
        driver.find_element_by_id("saveProduct").click()
        driver.refresh()
####################################################################################################################
#        testManId= Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("test").get_attribute("value")
#        print "testManId=\""+testManId+"\""

        driver.find_element_by_css_selector("div.bigDownArrow").click()
        testProduct1Id = driver.find_element_by_xpath("//ul[@id='productBrowser']/li[1]").get_attribute("id")
        testProduct1IdValue = re.sub("\D","",testProduct1Id)
        print "testProduct1IdValue=\""+ testProduct1IdValue+"\""

        testProduct2Id = driver.find_element_by_xpath("//ul[@id='productBrowser']/li[2]").get_attribute("id")
        testProduct2IdValue = re.sub("\D","",testProduct2Id)
        print "testProduct2IdValue=\""+ testProduct2IdValue+"\""

        testAcc1Id = driver.find_element_by_xpath("//ul[@id='productBrowser']/li[3]").get_attribute("id")
        testAcc1IdValue = re.sub("\D","",testAcc1Id)
        print "testAcc1IdValue=\""+ testAcc1IdValue+"\""

        testAcc2Id = driver.find_element_by_xpath("//ul[@id='productBrowser']/li[4]").get_attribute("id")
        testAcc2IdValue = re.sub("\D","",testAcc2Id)
        print "testAcc2IdValue=\""+ testAcc2IdValue+"\""

        print "Please record the testProduct1IdValue, testProduct2IdValue, testAcc1IdValue, testAcc2IdValue in the ids.py."
        print "Please go to setup Users Or Groups page, assign user group ztestUserGroup to assignStore"

        text_file = open(gb_Preprocess_ids_Prefix+"ids.py", "a")
#        ids =[]
        text_file.write("testProduct1IdValue=\""+ testProduct1IdValue+"\"\n")
        text_file.write("testProduct2IdValue=\""+ testProduct2IdValue+"\"\n")
        text_file.write("testAcc1IdValue=\""+ testAcc1IdValue+"\"\n")
        text_file.write("testAcc2IdValue=\""+ testAcc2IdValue+"\"\n")
#        text_file.write("testManId=\""+testManId+"\"")
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
