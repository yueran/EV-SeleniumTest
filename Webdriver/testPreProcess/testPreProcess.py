

#The purpose of this file is to go throught the preprocess for the selenium test. It would create necessary users, store groups etc for the test.
#Corresponding id for each elememets should be recorded in the test.




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import unittest, time, re
from selenium.webdriver import ActionChains
#import HTMLTestRunner
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *
from Webdriver.HTMLTestRunner import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
#from Webdriver.testPreProcess import createTestUser as PreProcessStep1
#from Webdriver.testPreProcess import assignUsersToGroups as preProcessStep2
#from Webdriver.testPreProcess import assignPremissions as PreProcessStep3
#from Webdriver.testPreProcess import createStoreHierarchy as PreProcessStep4
from Webdriver.testPreProcess import createCSCKeyWords as preProcessStep5
from Webdriver.testPreProcess import createLoops as preProcessStep6
from Webdriver.testPreProcess import createMedia as preProcessStep7
from Webdriver.testPreProcess import createProducts as preProcessStep8
from Webdriver.testPreProcess import createTemplates as preProcessStep9
from Webdriver.testPreProcess import createTestUsersAndGroups as preProcessStep10


def setUp(self):
    gb_setUp(self)

#class createTestUser(PreProcessStep1.createTestUser):
#
#    def test_create_test_user(self):
#        PreProcessStep1.createTestUser.test_create_test_user(sel

#class assignUserToGroups(PreProcessStep2.assignUserToGroups):
#
#    def test_assign_user_to_groups(self):
#        PreProcessStep2.assignUserToGroupsdef.test_assign_user_to_groups(self)

#class assignPermissions(PreProcessStep3.assignPermissions):
#    def test_assign_permissions(self):
#        PreProcessStep3.assignPermissions.test_assign_permissions(self)

#class createStoreHierarchy(PreProcessStep4.createStoreHierarchy):
#    def test_create_store_hierarchy(self):
#        PreProcessStep4.createStoreHierarchy.test_create_store_hierarchy(self)

class createCSCKeywords(preProcessStep5.createCSCKeywords):
    def test_create_csc_keywords(self):
        preProcessStep5.createCSCKeywords.test_create_csc_keywords(self)

class createLoops(preProcessStep6.createLoops):
    def test_create_loops(self):
        preProcessStep6.createLoops.test_create_loops(self)

class createMedia(preProcessStep7.createMedia):
    def test_create_media(self):
        preProcessStep7.createMedia.test_create_media(self)

class createProducts(preProcessStep8.createProducts):
    def test_create_products(self):
        preProcessStep8.createProducts.test_create_products(self)

class createTemplates(preProcessStep9.createTemplates):
    def test_create_templates(self):
        preProcessStep9.createTemplates.test_create_templates(self)

class createTestUsersAndGroups(preProcessStep10.createTestUsersAndGroups):
    def test_create_test_users_and_groups(self):
        preProcessStep10.createTestUsersAndGroups.test_create_test_users_and_groups(self)

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

#    testsuite.addTest(createTestUser("test_create_test_user"))
#    testsuite.addTest(assignUserToGroups("test_assign_user_to_groups"))
#    testsuite.addTest(assignPermissions("test_assign_permissions"))
#    testsuite.addTest(createStoreHierarchy("test_create_store_hierarchy"))
    testsuite.addTest(createCSCKeywords("test_create_csc_keywords"))
    testsuite.addTest(createLoops("test_create_loops"))
    testsuite.addTest(createMedia("test_create_media"))
    testsuite.addTest(createProducts("test_create_products"))
    testsuite.addTest(createTemplates("test_create_templates"))
    testsuite.addTest(createTestUsersAndGroups("test_create_test_users_and_groups"))


    filename = gb_Preprocess_Result_Prefix+'/PreprocessResults.html'
    fp = file(filename,'wb')

#    runner = HTMLTestRunner.HTMLTestRunner(
    runner =HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
