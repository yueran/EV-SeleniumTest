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

        driver.get(self.base_url + "/ev/createloops")

	driver.find_element_by_css_selector("div.createNewLoop.commonButton").click()
        driver.find_element_by_id("loopName").clear()
        driver.find_element_by_id("loopName").send_keys(assignLoops)
        driver.find_element_by_id("attractLoopPopupOK").click()

        assignLoopsId = driver.find_element_by_xpath("//ul[@class='loopList genericBrowser']/li[last()]").get_attribute("id")
        print "assignLoopsId=\""+assignLoopsId+"\""
        assignLoopsIdValue = re.sub("\D","",assignLoopsId)
        print "assignLoopsIdValue=\""+assignLoopsIdValue+"\""
        driver.refresh()

	driver.find_element_by_css_selector("div.createNewLoop.commonButton").click()
        driver.find_element_by_id("loopName").clear()
        driver.find_element_by_id("loopName").send_keys(editLoopSchedule)
        driver.find_element_by_id("attractLoopPopupOK").click()

        editLoopScheduleId = driver.find_element_by_xpath("//ul[@class='loopList genericBrowser']/li[last()]").get_attribute("id")
        print "editLoopScheduleId=\""+editLoopScheduleId+"\""
        editLoopScheduleIdValue = re.sub("\D","",editLoopScheduleId)
        print "editLoopScheduleIdValue=\""+editLoopScheduleIdValue+"\""
        driver.refresh()

	driver.find_element_by_css_selector("div.createNewLoop.commonButton").click()
        driver.find_element_by_id("loopName").clear()
        driver.find_element_by_id("loopName").send_keys(editNameOfLoop)
        driver.find_element_by_id("attractLoopPopupOK").click()

        editNameOfLoopId = driver.find_element_by_xpath("//ul[@class='loopList genericBrowser']/li[last()]").get_attribute("id")
        print "editNameOfLoopId=\""+editNameOfLoopId+"\""
        editNameOfLoopIdValue = re.sub("\D","",editNameOfLoopId)
        print "editNameOfLoopIdValue=\""+editNameOfLoopIdValue+"\""
        driver.refresh()

        print "Please record the editNameOfLoopId, editLoopSchedule and assignLoops in the ids.py."



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()