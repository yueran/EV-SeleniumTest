from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnSetupUsersOrGroupsFunctionUsersCreateUsers(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_users_create_users(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        try: self.assertNotIn(setupUsersOrGroupsCreateUser,driver.find_element_by_class_name("userColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.createNewUser.commonButton").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(setupUsersOrGroupsCreateUserFirstNameSendKeys)
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys(setupUsersOrGroupsCreateUserLastNameSendKeys)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(setupUsersOrGroupsCreateUserEmailSendKeys)
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(setupUsersOrGroupsCreateUserUserName)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(setupUsersOrGroupsCreateUserPasswordSendKeys)
        driver.find_element_by_id("repeatPassword").clear()
        driver.find_element_by_id("repeatPassword").send_keys(setupUsersOrGroupsCreateUserRepeatPasswordSendKeys)
        driver.find_element_by_id("okSingleUser").click()
#        try: self.assertIn(setupUsersOrGroupsCreateUser,driver.find_element_by_class_name("userColumn").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        try: self.assertIn(setupUsersOrGroupsCreateUser,driver.find_element_by_class_name("userColumn").text)
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
