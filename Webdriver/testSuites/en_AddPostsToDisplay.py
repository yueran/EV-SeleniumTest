#This one should be tested together with test case 'en_AddPostsToDisplay_SelectADevice'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import HTMLTestRunner
from Webdriver.HTMLTestRunner import *
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
from Webdriver.contentMaintenance import *
from Webdriver.testCase.functionalTesting.addPostsToDisplay import en_AddPostsToDisplay_contentVerification as TestCase1
from Webdriver.testCase.functionalTesting.addPostsToDisplay import en_AddPostsToDisplay_Help as TestCase2
from Webdriver.testCase.functionalTesting.addPostsToDisplay import en_AddPostsToDisplay_SelectADevice as TestCase3
from Webdriver.testCase.functionalTesting.addPostsToDisplay import en_AddPostsToDisplay_IdentifyDevice as TestCase4

def setUp(self):
        gb_setUp(self)
        
#TestCase1: content verification
class EnAddPostsToDisplayContentVerification(TestCase1.EnAddPostsToDisplayContentVerification):
    def test_en_add_posts_to_display_content_verification(self):
        TestCase1.EnAddPostsToDisplayContentVerification.test_en_add_posts_to_display_content_verification(self)
#TestCase2: help content
class EnAddPostsToDisplayHelpContent(TestCase2.EnAddPostsToDisplayHelpContent):
    def test_en_add_posts_to_display_help_content(self):
        TestCase2.EnAddPostsToDisplayHelpContent.test_en_add_posts_to_display_help_content(self)

#TestCase3:Select a device
class EnAddPostsToDisplaySelectADevice(TestCase3.EnAddPostsToDisplaySelectADevice):
    def test_en_add_posts_to_display_select_a_device(self):
        TestCase3.EnAddPostsToDisplaySelectADevice.test_en_add_posts_to_display_select_a_device(self)

#TestCase4:Identify a device
class EnAddPostsToDisplayIdentifyDevice(TestCase4.EnAddPostsToDisplayIdentifyDevice):
    def test_en_add_posts_to_display_identify_device(self):
        TestCase4.EnAddPostsToDisplayIdentifyDevice.test_en_add_posts_to_display_identify_device(self)

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnAddPostsToDisplayContentVerification("test_en_add_posts_to_display_content_verification"))
    testsuite.addTest(EnAddPostsToDisplayHelpContent("test_en_add_posts_to_display_help_content"))
    testsuite.addTest(EnAddPostsToDisplaySelectADevice("test_en_add_posts_to_display_select_a_device"))
    testsuite.addTest(EnAddPostsToDisplayIdentifyDevice("test_en_add_posts_to_display_identify_device"))


    filename = gb_filename_prefix+'/AddPostsToDisplay.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
