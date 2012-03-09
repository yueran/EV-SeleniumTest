from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.Index import en_Index_Verification as IndexCase1
from Webdriver.testCase.functionalTesting.Index import en_Index_HelpContent as IndexCase2

def setUp(self):
    gb_setUp(self)

class EnIndexVerification(IndexCase1.EnIndexVerification):
    def test_en_index_verification(self):
        IndexCase1.EnIndexVerification.test_en_index_verification(self)

class EnIndexHelpContent(IndexCase2.EnIndexHelpContent):
    def test_en_index_help_content(self):
        IndexCase2.EnIndexHelpContent.test_en_index_help_content(self)

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnIndexVerification("test_en_index_verification"))
    testsuite.addTest(EnIndexHelpContent("test_en_index_help_content"))


    filename = gb_filename_prefix+'/Index.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
