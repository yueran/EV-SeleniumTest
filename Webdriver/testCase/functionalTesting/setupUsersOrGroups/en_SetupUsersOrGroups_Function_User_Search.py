from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnSetupUsersOrGroupsFunctionUsersSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_setup_users_or_groups_function_users_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/setupusersorgroups")
        try: self.assertIn(setupUsersOrGroupsSearchUser1, driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(setupUsersOrGroupsSearchUser2, driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertIn(u"Modify", driver.find_element_by_id("usrBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterTextUserColumn").clear()
        driver.find_element_by_id("filterTextUserColumn").send_keys(setupUsersOrGroupsSearchUserKey1)
        try: self.assertIn(setupUsersOrGroupsSearchUser1, driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(setupUsersOrGroupsSearchUser2, driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertNotIn(u"Modify", driver.find_element_by_id("usrBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterTextUserColumn").clear()
        driver.find_element_by_id("filterTextUserColumn").send_keys("")
        Select(driver.find_element_by_id("filterUserColumn")).select_by_visible_text("User Name")
        driver.find_element_by_id("filterTextUserColumn").send_keys(setupUsersOrGroupsSearchUserKey1)
        driver.find_element_by_xpath("//div[@id='usersSpace']/div/span[2]").click()
        try: self.assertIn(setupUsersOrGroupsSearchUser1, driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(setupUsersOrGroupsSearchUser2, driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertNotIn(u"Modify", driver.find_element_by_id("usrBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterTextUserColumn").clear()
        Select(driver.find_element_by_id("filterUserColumn")).select_by_visible_text("First Name")
        driver.find_element_by_id("filterTextUserColumn").send_keys(setupUsersOrGroupsSearchUserKey1)
        for i in range(60):
            try:
                if "\""+searchUserLastName+", "+searchUserFirstName+"\"" == driver.find_element_by_xpath("//li[@id='users_user"+searchUserIdValue +"']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn("\""+searchUserLastName+", "+searchUserFirstName+"\"", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("\""+editUserLastName+", "+editUserFirstName+"\"", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertNotIn(u"Modify", driver.find_element_by_id("usrBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterTextUserColumn").clear()
        Select(driver.find_element_by_id("filterUserColumn")).select_by_visible_text("Last Name")
        driver.find_element_by_id("filterTextUserColumn").send_keys(editUserName)
        for i in range(60):
            try:
                if "\""+editUserLastName+", "+editUserFirstName+"\"" == driver.find_element_by_xpath("//li[@id='users_user"+editUserIdValue+"']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn("\""+searchUserLastName+", "+searchUserFirstName+"\"", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("\""+editUserLastName+", "+editUserFirstName+"\"", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertNotIn(u"Modify", driver.find_element_by_id("usrBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("filterTextUserColumn").clear()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
