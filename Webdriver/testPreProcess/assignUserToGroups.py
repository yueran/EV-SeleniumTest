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


class assignUserToGroups(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_assign_user_to_groups(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("")
        driver.find_element_by_id("form.login").clear()
        driver.find_element_by_id("form.login").send_keys("andrew")
        driver.find_element_by_id("form.password").clear()
        driver.find_element_by_id("form.password").send_keys("andrew")
        driver.find_element_by_css_selector("span.commonButton.login_ok").click()
        gb_frame(self)

        driver.get(self.base_url + "/ev/setupusersorgroups")
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='users_user"+testUserIdValue+"']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='userGroup_userGroup"+testUserGroupIdValue+"']"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        element = driver.find_element_by_xpath("//li[@id='users_user"+testUserIdValue+"']/div/div")
        target = driver.find_element_by_xpath("//li[@id='userGroup_userGroup"+testUserGroupIdValue+"']")
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(element)
        action_chains.move_to_element(target)
#        action_chains.perform()
#        driver.mouse_down_at(element)
#        driver.mouse_move_at(target)
#        driver.mouse_up_at(element)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
