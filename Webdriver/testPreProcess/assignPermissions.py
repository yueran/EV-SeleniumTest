# To change this template, choose Tools | Templates
# and open the template in the editor.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


import unittest, time, re
from selenium.webdriver import ActionChains
#import HTMLTestRunner
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *
#from Webdriver.testPreProcess.createTestUser import *

class assignPermissions(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_assign_permissions(self):
        global testUserId, testUserIdValue, testUserGroupId, testUserGroupIdValue
        driver = self.driver
        driver.get(self.base_url + "/ev/login")

        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys("andrew")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("andrew")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()

        driver.get(self.base_url + "/ev/setupusersorgroups")
##        print "testUserGroupIdValue="+createTestUser.testUserGroupIdValue
#        driver.find_element_by_id("userGroup_userGroupOptions"+createTestUser.testUserGroupIdValue).click()
        
        driver.find_element_by_id("userGroup_userGroupOptions"+testUserGroupIdValue).click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#createAttractLoopsPerms']").click()
        driver.find_element_by_id("createAttractLoopsPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#scheduleTemplatesPerms']").click()
        driver.find_element_by_id("scheduleTemplatesPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#templateStylesPerms']").click()
        driver.find_element_by_id("templateStylesPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#createProductsPerms']").click()
        driver.find_element_by_id("createProductsPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#mediaManagerPerms']").click()
        driver.find_element_by_id("mediaManagerPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#groupMediaPlayersPerms']").click()
        driver.find_element_by_id("groupMediaPlayersPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#networkManagerPerms']").click()
        driver.find_element_by_id("networkManagerPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#assignAccessoriesPerms']").click()
        driver.find_element_by_id("assignAccessoriesPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#storeHierarchyPerms']").click()
        driver.find_element_by_id("storeHierarchyPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#createReportsPerms']").click()
        driver.find_element_by_id("createReportsPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#assignPermissionsPerms']").click()
        driver.find_element_by_id("assignPermissionsPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#scheduleAttractLoopsPerms']").click()
        driver.find_element_by_id("scheduleAttractLoopsPermsChkBox").click()
        driver.find_element_by_xpath("//div[@id='permissions']//li/a[@href='#classifyProductsPerms']").click()
        driver.find_element_by_id("classifyProductsPermsChkBox").click()
        driver.find_element_by_id("okUserGroupOptions").click()

        driver.find_element_by_id("userGroup_userGroupOptions"+testUserGroupIdValue).click()
        driver.find_element_by_link_text("Create Attract Loops").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("createAttractLoopsPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Schedule Templates").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("scheduleTemplatesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Template Styles").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("templateStylesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Create Products").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("createProductsPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Media Manager").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("mediaManagerPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Group Media Players").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("groupMediaPlayersPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Network Manager").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("networkManagerPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Assign Accessories").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("assignAccessoriesPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Store Hierarchy").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("storeHierarchyPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Assign Permissions").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("assignPermissionsPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Create Reports").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("createReportsPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Schedule Loops").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("scheduleAttractLoopsPermsChkBox").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Classify Products").click()
        self.driver.implicitly_wait(30)
        try: self.assertEqual("on", driver.find_element_by_id("scheduleAttractLoopsPermsChkBox").get_attribute("value"))
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
