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

class createStoreHierarchy(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_store_hierarchy(self):
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

        driver.get(self.base_url + "/ev/storehierarchy")

        driver.find_element_by_id("newCompany").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(companyTest)
        driver.find_element_by_id("renameOK").click()
        companyTestId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[last()]").get_attribute("id")
        companyTestIdValue = re.sub("\D","",companyTestId)
#        print "companyTestId="+companyTestId
#        print "companyTestIdValue="+companyTestIdValue
#
#        for i in range(60):
#            try:
#                if companyTest == driver.find_element_by_xpath("//li[@id='hierarchy_company"+companyTestIdValue +"']/div/div[2]").text: break
#            except: pass
#            time.sleep(1)
#        else: self.fail("time out")
#        try: self.assertIn(companyTest, driver.find_element_by_class_name("genericBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#	self.driver.implicitly_wait(30)
        driver.refresh()
        driver.get(self.base_url + "/ev/storehierarchy")
        driver.find_element_by_id("newStoreGroup").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeGroupTest)
        driver.find_element_by_id("renameOK").click()
#        storeGroupTestId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[last()]").get_attribute("id")
#        storeGroupTestIdValue = re.sub("\D","",storeGroupTestId)

#        try: self.assertIn(storeGroupTest, driver.find_element_by_class_name("genericBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        print "storeGroupTestId="+storeGroupTestId
#        print "storeGroupTestIdValue="+storeGroupTestIdValue
	self.driver.implicitly_wait(30)
        driver.refresh()

        driver.get(self.base_url + "/ev/storehierarchy")
        driver.find_element_by_id("newStore").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(storeTest)
        driver.find_element_by_id("renameOK").click()
#        storeTestId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[last()]").get_attribute("id")
#        storeTestIdValue = re.sub("\D","",storeTestId)
#
#        print "storeTestId="+storeTestId
#        print "storeTestIdValue="+storeTestIdValue
	self.driver.implicitly_wait(30)
        driver.refresh()

        driver.get(self.base_url + "/ev/storehierarchy")
        driver.find_element_by_id("newStore").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(dStore)
        driver.find_element_by_id("renameOK").click()
#        dStoreId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[last()]").get_attribute("id")
#        dStoreIdValue = re.sub("\D","",dStoreId)
#
#        print "dStore="+dStoreId
#        print "dStoreIdValue="+dStoreIdValue
	self.driver.implicitly_wait(30)
        driver.refresh()

        driver.get(self.base_url + "/ev/storehierarchy")
        driver.find_element_by_id("newStore").click()
        driver.find_element_by_id("rename").clear()
        driver.find_element_by_id("rename").send_keys(assignStore)
        driver.find_element_by_id("renameOK").click()
#        assignStoreId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[last()]").get_attribute("id")
#        assignStoreIdValue = re.sub("\D","",assignStoreId)

##############################################################################################################################
        companyTestId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[1]").get_attribute("id")
        companyTestIdValue = re.sub("\D","",companyTestId)
#        print "companyTestId="+companyTestId
        print "companyTestIdValue=\""+companyTestIdValue+"\""

        storeGroupTestId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[2]").get_attribute("id")
        storeGroupTestIdValue = re.sub("\D","",storeGroupTestId)
#        print "storeGroupTestId="+storeGroupTestId
        print "storeGroupTestIdValue=\""+storeGroupTestIdValue+"\""

        storeTestId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[3]").get_attribute("id")
        storeTestIdValue = re.sub("\D","",storeTestId)

#        print "storeTestId="+storeTestId
        print "storeTestIdValue=\""+storeTestIdValue+"\""

        dStoreId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[4]").get_attribute("id")
        dStoreIdValue = re.sub("\D","",dStoreId)

#        print "dStore="+dStoreId
        print "dStoreIdValue=\""+dStoreIdValue+"\""

        assignStoreId = driver.find_element_by_xpath("//ul[@class='genericBrowser']/li[5]").get_attribute("id")
        assignStoreIdValue = re.sub("\D","",assignStoreId)
#        print "assignStore="+assignStoreId
        print "assignStoreIdValue=\""+assignStoreIdValue+"\""
	self.driver.implicitly_wait(30)
        driver.refresh()

        print "Please record the storeTestIdValue, storeGroupTestIdValue, assignStoreIdValue, dStoreIdValue and companyTest in the ids.py."
        print "Please go to setup Users Or Groups page, assign user group ztestUserGroup to assignStore"




    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
