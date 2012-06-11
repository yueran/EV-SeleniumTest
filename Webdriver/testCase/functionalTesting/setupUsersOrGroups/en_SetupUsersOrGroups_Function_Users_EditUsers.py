from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnSetupUsersOrGroupsFunctionUsersEditUsers(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_users_edit_users(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        try: self.assertIn(setupUsersOrGroupsEditUser,driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(setupUsersOrGroupsEditUserModified,driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("users_userOptions"+setupUsersOrGroupsEditUserID).click()
        #driver.find_element_by_id("users_userOptions15").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(setupUsersOrGroupsEditUserModifiedFirstNameSendKeys)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(setupUsersOrGroupsEditUserModifiedLastNameSendKeys)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(setupUsersOrGroupsEditUserModifiedEmailSendKeys)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(setupUsersOrGroupsEditUserModifiedUserNameSendKeys)
        driver.find_element_by_id("okSingleUser").click()
        #driver.find_element_by_id("users_userOptions149").click()
        for i in range(60):
            try:
                if setupUsersOrGroupsEditUserModified == driver.find_element_by_css_selector("#users_user"+setupUsersOrGroupsEditUserID+" > div.userBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.driver.implicitly_wait(30)
        try: self.assertNotIn(setupUsersOrGroupsEditUser,driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(setupUsersOrGroupsEditUserModified,driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("users_userOptions"+setupUsersOrGroupsEditUserID).click()
        #driver.find_element_by_id("users_userOptions15").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(setupUsersOrGroupsEditUserFirstNameSendKeys)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(setupUsersOrGroupsEditUserLastNameSendKeys)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(setupUsersOrGroupsEditUserUserNameSendKeys)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(setupUsersOrGroupsEditUserEmailSendKeys)
        driver.find_element_by_id("okSingleUser").click()
        self.driver.implicitly_wait(30)
        for i in range(60):
            try:
                if setupUsersOrGroupsEditUser == driver.find_element_by_css_selector("#users_user"+setupUsersOrGroupsEditUserID+" > div.userBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.driver.implicitly_wait(30)
        try: self.assertIn(setupUsersOrGroupsEditUser,driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(setupUsersOrGroupsEditUserModified,driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("users_userOptions"+setupUsersOrGroupsEditUserID).click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
