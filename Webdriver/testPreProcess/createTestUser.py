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

class createTestUser(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_test_user(self):
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
        try: self.assertNotIn("\""+userLastName+", "+userFirstName+"\"", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.createNewUser.commonButton").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(userFirstName)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(userLastName)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(userEmailAdd)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(userName)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(userPassword)
        driver.find_element_by_id("repeatPassword").clear()
        driver.find_element_by_id("repeatPassword").send_keys(userPasswordRepeat)
        driver.find_element_by_id("okSingleUser").click()


#        for i in range(60):
#            try:
#                if userLastName+", "+userFirstName == driver.find_element_by_xpath("//li[@id='users_user"+testUserIdValue +"']/div/div[2]").text: break
#            except: pass
#            time.sleep(1)
#        else: self.fail("time out")
#
#
#        try: self.assertIn(userLastName+", "+userFirstName, driver.find_element_by_id("usrBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))


    #####################################################################################################
    #Create test user group:
        driver.find_element_by_css_selector("div.createNewUserGroup.commonButton").click()
        driver.find_element_by_id("userGroupName").clear()
        driver.find_element_by_id("userGroupName").send_keys(userGroupName)
        driver.find_element_by_id("okUserGroupOptions").click()
        self.driver.implicitly_wait(30)
        driver.refresh()
        driver.get(self.base_url + "/ev/setupusersorgroups")
#        try: self.assertIn(userGroupName,driver.find_element_by_class_name("userGroupColumn").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))

#        testUserGroupId = driver.find_element_by_xpath("//ul[@class='userGroupList genericBrowser']/li[last()]").get_attribute("id")
#        print "testUserGroupId="+testUserGroupId
#        testUserGroupIdValue = re.sub("\D","",testUserGroupId)
#        print "testUserGroupIdValue=\""+testUserGroupIdValue+"\""

#        for i in range(60):
#            try:
#                if userGroupName == driver.find_element_by_xpath("//li[@id='userGroup_userGroup"+testUserGroupIdValue+"']/div/div[2]").text: break
#            except: pass
#            time.sleep(1)
#        else: self.fail("time out")

#
#        try: self.assertIn(userGroupName, driver.find_element_by_class_name("userGroupList").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        print "Please record the testUserId, testUserIdValue, testUserGroupId and testUserGroupIdValue in the ids.py."


#######################################################################################################################################################
    #Assign user to user Groups:
#
#        target = driver.find_element_by_xpath("//li[@id='users_user"+testUserIdValue+"']/div/div")
#        element = driver.find_element_by_xpath("//li[@id='userGroup_userGroup"+testUserGroupIdValue+"']")
###        action_chains = ActionChains(driver)
###        action_chains.drag_and_drop(element, target);
###        time.sleep(15)
##        driver.mouse_down(target)
##        driver.mouse_move(element)
##        driver.mouse_up(target)
##        action_chains.drag_and_drop(target, element)
##        self.driver.implicitly_wait(30)
###        driver.mouse_down_at(target)
##        self.driver.implicitly_wait(30)
#        action_chains = ActionChains(driver)
#        action_chains.drag_and_drop(element, target).perform()
##        action_chains.click_and_hold(target)
#        action_chains.move_to_element(element)
#        self.driver.implicitly_wait(30)
##        action_chains.release(element)
#        for i in range(60):
#            try:
#                if userLastName+", "+userFirstName == driver.find_element_by_xpath("//li[@id='userGroup_user"+testUserIdValue+"']/div/div[2]").text: break
#            except: pass
#            time.sleep(1)
#        else: self.fail("time out")
#        self.driver.implicitly_wait(30)
#        action_chains.release(element)
#        self.driver.implicitly_wait(30)
##        action_chains.perform()
#################################################################################################################3
#
        testUserGroupId = driver.find_element_by_xpath("//ul[@class='userGroupList genericBrowser']/li[last()]").get_attribute("id")
#        print "testUserGroupId="+testUserGroupId
        testUserGroupIdValue = re.sub("\D","",testUserGroupId)
        print "testUserGroupIdValue=\""+testUserGroupIdValue+"\""

        testUserId = driver.find_element_by_xpath("//ul[@id='usrBrowser']//li[last()]").get_attribute("id")
#        print "testUserId="+testUserId
        testUserIdValue = re.sub("\D","",testUserId)
        print "testUserIdValue=\""+testUserIdValue+"\""


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
