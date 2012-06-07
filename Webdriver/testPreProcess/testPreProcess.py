

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
from Webdriver.testPreProcess import createTestUser as PreProcessStep1

def setUp(self):
    gb_setUp(self)

class createTestUser(PreProcessStep1.createTestUser):
    
    def test_create_test_user(self):
        PreProcessStep1.createTestUser.test_create_test_user(self)
        

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(createTestUser("test_create_test_user"))
#    testsuite.addTest(EnIndexHelpContent("test_en_index_help_content"))


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
