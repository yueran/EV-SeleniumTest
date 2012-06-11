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

testUserId = None
testUserIdValue = None
testUserGroupId = None
testUserGroupIdValue = None

class createMedia(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_create_media(self):
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

        driver.get(self.base_url + "/ev/uploadmedia")
        try: self.assertNotIn(ModifyMediaGroup, driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(TestMediaGroup, driver.find_element_by_id("mediaGroupBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_css_selector("div.createNewMediaGroup.commonButton").click()
        driver.find_element_by_id("mediaGroupName").clear()
        driver.find_element_by_id("mediaGroupName").send_keys(ModifyMediaGroup)
        driver.find_element_by_id("mediaGroupPopupOK").click()
        driver.refresh()


        driver.refresh()
#        for i in range(60):
#            try:
#                if ModifyMediaGroup == driver.find_element_by_css_selector("#mediaGroup_mediaGroup"+ModifyMediaGroupIdValue +"> div.mediaGroupBg.itemContent > div.blockText").text: break
#            except: pass
#            time.sleep(1)
#        else: self.fail("time out")
        driver.get(self.base_url + "/ev/uploadmedia")
        driver.find_element_by_css_selector("div.createNewMediaGroup.commonButton").click()
        driver.find_element_by_id("mediaGroupName").clear()
        driver.find_element_by_id("mediaGroupName").send_keys(TestMediaGroup)
        driver.find_element_by_id("mediaGroupPopupOK").click()
        driver.refresh()

#        for i in range(60):
#            try:
#                if ModifyMediaGroup == driver.find_element_by_css_selector("#mediaGroup_mediaGroup"+ModifyMediaGroupIdValue +"> div.mediaGroupBg.itemContent > div.blockText").text: break
#            except: pass
#            time.sleep(1)
#        else: self.fail("time out")
#        try: self.assertIn(ModifyMediaGroup, driver.find_element_by_id("mediaGroupBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertIn(TestMediaGroup, driver.find_element_by_id("mediaGroupBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))



############################################################################################################
        print "Please record the ModifyMediaGroupIdValue, TestMediaGroupIdValue in the ids.py."
        ModifyMediaGroupId = driver.find_element_by_xpath("//ul[@id='mediaGroupBrowser']/li[1]").get_attribute("id")
#        print "ModifyMediaGroupId="+ModifyMediaGroupId
        ModifyMediaGroupIdValue = re.sub("\D","",ModifyMediaGroupId)
        print "ModifyMediaGroupIdValue=\""+ModifyMediaGroupIdValue+"\""

        TestMediaGroupId = driver.find_element_by_xpath("//ul[@id='mediaGroupBrowser']/li[2]").get_attribute("id")
#        print "TestMediaGroupId="+TestMediaGroupId
        TestMediaGroupIdValue = re.sub("\D","",TestMediaGroupId)
        print "TestMediaGroupIdValue=\""+TestMediaGroupIdValue+"\""

        text_file = open(gb_Preprocess_ids_Prefix+"ids.py", "a")
#        ids =[]
        text_file.write("ModifyMediaGroupIdValue=\""+ModifyMediaGroupIdValue+"\"\n")
        text_file.write("TestMediaGroupIdValue=\""+TestMediaGroupIdValue+"\"\n")
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
