#Still has some problem with the drag and drop function testing.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *


class EnSetupUsersOrGroupsFunctionAssignUassignUserGroup(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_assign_uassign_user_group(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        try: self.assertTrue(self.is_element_present(By.XPATH, "//li[@id='userGroup_userGroup"+setupUsersOrGroupsUserGroupID+"']/div/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_xpath("//li[@id='hierarchy_storeGroup202']/div/span").click()
        #try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#hierarchy_store203 > div.itemContent.storeBg > div.blockText"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#hierarchy_store"+setupUsersOrGroupsAssginStoreID+" > div.itemContent.storeBg > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        element = driver.find_element_by_xpath("//li[@id='userGroup_userGroup"+setupUsersOrGroupsUserGroupID+"']/div/div")
        target = driver.find_element_by_css_selector("#hierarchy_store"+setupUsersOrGroupsAssginStoreID+" > div.itemContent.storeBg > div.blockText")
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(element, target);
        #driver.find_element_by_xpath("//li[@id='hierarchy_store203']/div/span").click()
        #try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#store203_userGroup172 > div.itemContent.userGroupBg > span.unassign"))
        #except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_css_selector("#store203_userGroup172 > div.itemContent.userGroupBg > span.unassign").click()
        #driver.find_element_by_css_selector("#hierarchy_storeGroup202 > div.itemContent.storeGroupBg > span.fold").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
