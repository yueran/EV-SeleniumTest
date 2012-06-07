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
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys(userName)
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys(userPassword)
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()

        driver.get(self.base_url + "/ev/setupusersorgroups")
######create other test user:

        driver.find_element_by_css_selector("div.createNewUser.commonButton").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(searchUserFirstName)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(searchUserLastName)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(searchUserEmailAdd)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(searchUserName)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(userPassword)
        driver.find_element_by_id("repeatPassword").clear()
        driver.find_element_by_id("repeatPassword").send_keys(userPasswordRepeat)
        driver.find_element_by_id("okSingleUser").click()
        driver.refresh()

#####edit user:


        driver.find_element_by_css_selector("div.createNewUser.commonButton").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(editUserFirstName)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(editUserLastName)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(editUserEmailAdd)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(editUserName)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(userPassword)
        driver.find_element_by_id("repeatPassword").clear()
        driver.find_element_by_id("repeatPassword").send_keys(userPasswordRepeat)
        driver.find_element_by_id("okSingleUser").click()
        driver.refresh()


    #####################################################################################################

###DuplicateUserGroup
        driver.find_element_by_css_selector("div.createNewUserGroup.commonButton").click()
        driver.find_element_by_id("userGroupName").clear()
        driver.find_element_by_id("userGroupName").send_keys(duplicateUserGroup)
        driver.find_element_by_id("okUserGroupOptions").click()
        self.driver.implicitly_wait(30)
        driver.refresh()
        try: self.assertIn(userGroupName,driver.find_element_by_class_name("userGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

###EditUserGroup
        driver.find_element_by_css_selector("div.createNewUserGroup.commonButton").click()
        driver.find_element_by_id("userGroupName").clear()
        driver.find_element_by_id("userGroupName").send_keys(editUserGroup)
        driver.find_element_by_id("okUserGroupOptions").click()
        self.driver.implicitly_wait(30)
        driver.refresh()
        try: self.assertIn(userGroupName,driver.find_element_by_class_name("userGroupColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))


#########################################################################################################################
        editUserId = driver.find_element_by_xpath("//ul[@id='usrBrowser']//li[2]").get_attribute("id")
#        print "editUserId=\""+editUserId+"\""
        editUserIdValue = re.sub("\D","",editUserId)
        print "editUserIdValue=\""+editUserIdValue+"\""
        duplicateUserGroupId = driver.find_element_by_xpath("//ul[@class='userGroupList genericBrowser']/li[1]").get_attribute("id")
#        print "duplicateUserGroupId="+duplicateUserGroupId
        duplicateUserGroupIdValue = re.sub("\D","",duplicateUserGroupId)
        print "duplicateUserGroupIdValue=\""+duplicateUserGroupIdValue+"\""
        editUserGroupId = driver.find_element_by_xpath("//ul[@class='userGroupList genericBrowser']/li[2]").get_attribute("id")
#        print "editUserGroupId="+editUserGroupId
        editUserGroupIdValue = re.sub("\D","",editUserGroupId)
        print "editUserGroupIdValue=\""+editUserGroupIdValue+"\""




    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
