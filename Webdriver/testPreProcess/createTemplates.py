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


class createTemplates(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_templates(self):
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

        driver.get(self.base_url + "/ev/templatestyles")

        driver.find_element_by_id("newTemplate").click()

        driver.find_element_by_id("templateEditName").clear()
        driver.find_element_by_id("templateEditName").send_keys(editTmpSchedule)
        driver.find_element_by_id("buttonLeftPopup").click()
        driver.find_element_by_id("touchPopup").click()
        driver.find_element_by_id("createTemplate").click()

        driver.refresh()

        driver.find_element_by_id("newTemplate").click()

        driver.find_element_by_id("templateEditName").clear()
        driver.find_element_by_id("templateEditName").send_keys(duplicateTmp)
        driver.find_element_by_id("buttonLeftPopup").click()
        driver.find_element_by_id("touchPopup").click()
        driver.find_element_by_id("createTemplate").click()

        driver.find_element_by_id("newTemplate").click()

        driver.find_element_by_id("templateEditName").clear()
        driver.find_element_by_id("templateEditName").send_keys(modifyTmp)
        driver.find_element_by_id("buttonLeftPopup").click()
        driver.find_element_by_id("touchPopup").click()
        driver.find_element_by_id("createTemplate").click()

        driver.refresh()

        duplicateTmpId = driver.find_element_by_xpath("//ul[@id='templateBrowser']/li[1]").get_attribute("id")
#        print "duplicateTmpId=\""+duplicateTmpId+"\""
        duplicateTmpIdValue = re.sub("\D","",duplicateTmpId)
        print "duplicateTmpIdValue=\""+duplicateTmpIdValue+"\""
        
        editTmpScheduleId = driver.find_element_by_xpath("//ul[@id='templateBrowser']/li[2]").get_attribute("id")
#        print "editTmpScheduleId=\""+editTmpScheduleId+"\""
        editTmpScheduleIdValue = re.sub("\D","",editTmpScheduleId)
        print "editTmpScheduleValue=\""+editTmpScheduleIdValue+"\""

        modifyTmpId = driver.find_element_by_xpath("//ul[@id='templateBrowser']/li[3]").get_attribute("id")
#        print "modifyTmp=\""+modifyTmp+"\""
        modifyTmpIdValue = re.sub("\D","",modifyTmpId)
        print "modifyTmpIdValue=\""+modifyTmpIdValue+"\""

        print "Please record the modifyTmpIdValue, duplicateTmpIdValue and editTmpScheduleIdValue in the ids.py."

        text_file = open(gb_Preprocess_ids_Prefix+"ids.py", "a")
#        ids =[]
        text_file.write("duplicateTmpIdValue=\""+duplicateTmpIdValue+"\"\n")
        text_file.write("editTmpScheduleValue=\""+editTmpScheduleIdValue+"\"\n")
        text_file.write("modifyTmpIdValue=\""+modifyTmpIdValue+"\"\n")

#        text_file.write(("".join(ids))+"\n")
        text_file.close()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
