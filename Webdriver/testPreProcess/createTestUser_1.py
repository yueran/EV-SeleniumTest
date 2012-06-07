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

class createTestUser(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_test_user(self):
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
        try: self.assertNotIn("yrtest2, yrtest2",driver.find_element_by_class_name("userColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.createNewUser.commonButton").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("yrtest2")
        driver.find_element_by_id("lastName").clear()
        driver.find_element_by_id("lastName").send_keys("yrtest2")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("yrtest2@gmail.com")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("yrtest2")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("repeatPassword").clear()
        driver.find_element_by_id("repeatPassword").send_keys("test")
        driver.find_element_by_id("okSingleUser").click()
        driver.refresh()
        try: self.assertIn("yrtest2, yrtest2",driver.find_element_by_class_name("userColumn").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        testUserId = driver.find_element_by_xpath("//ul[@id='usrBrowser']//li[last()]").get_attribute("id")
        print "testUserId="+testUserId
        testUserIdValue = re.sub("\D","",testUserId)
        for i in range(60):
            try:
                if "yrtest2, yrtest2" == driver.find_element_by_xpath("//li[@id='users_user"+testUserIdValue +"']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn("yrtest2, yrtest2", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("users_userOptions" + testUserIdValue).click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys("yrtest3")
        driver.find_element_by_id("okSingleUser").click()
        for i in range(60):
            try:
                if "yrtest2, yrtest3" == driver.find_element_by_xpath("//li[@id='users_user"+testUserIdValue +"']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn("yrtest2, yrtest3", driver.find_element_by_id("usrBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("users_userDelete" + testUserIdValue).click()
        for i in range(60):
            try:
                if "Delete yrtest2, yrtest3" == driver.find_element_by_id("popup_title").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.driver.implicitly_wait(30)
        try: self.assertIn("Are you sure you want to remove the User", driver.find_element_by_id("popup_container").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("popup_ok").click()

        for i in range(60):
            try:
                if "cd, ab" == driver.find_element_by_xpath("//li[@id='users_user46']/div/div[2]").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn("yrtest2, yrtest3", driver.find_element_by_id("usrBrowser").text)
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
