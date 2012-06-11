# coding: utf-8
#note: this test suite is not fully complished. Detailed functions have not been input in the test case
#like the background color,border etc in Logo, large image, small image etc.
#Need to delete the created template(CreateTmp) manually after testing.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.HTMLTestRunner import *
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_Function_CreateTemplates as TestCase3
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_Function_DuplicateTmp as TestCase4
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_Function_ModifyTmp_Content_Logo as TestCase5
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_Function_ModifyTmp_Content_touch_nontouch as TestCase6
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_Function_ModifyTmp_Name as TestCase7
from Webdriver.testCase.functionalTesting.templateStyles import en_TemplateStyle_Function_Search as TestCase8


def setUp(self):
    gb_setUp(self)
    
class EnTemplateStyleContentVerification(TestCase1.EnTemplateStyleContentVerification):
    def test_en_template_style_content_verification(self):
        TestCase1.EnTemplateStyleContentVerification.test_en_template_style_content_verification(self)

class EnTemplateStyleContentVerificationHelp(TestCase2.EnTemplateStyleContentVerificationHelp):
    def test_en_template_style_content_verification_help(self):
        TestCase2.EnTemplateStyleContentVerificationHelp.test_en_template_style_content_verification_help(self)

class EnTemplateStyleFunctionCreateTemplates(TestCase3.EnTemplateStyleFunctionCreateTemplates):
    def test_en_template_style_function_create_templates(self):
        TestCase3.EnTemplateStyleFunctionCreateTemplates.test_en_template_style_function_create_templates(self)

class EnTemplateStyleFunctionDuplicateTmp(TestCase4.EnTemplateStyleFunctionDuplicateTmp):
    def test_en_template_style_function_duplicate_tmp(self):
        TestCase4.EnTemplateStyleFunctionDuplicateTmp.test_en_template_style_function_duplicate_tmp(self)
#This test case is pending: have problem with 'double-click'
class EnTemplateStyleFunctionModifyTmpContentLogo(TestCase5.EnTemplateStyleFunctionModifyTmpContentLogo):
    def test_en_template_style_function_modify_tmp_content_logo(self):
        TestCase5.EnTemplateStyleFunctionModifyTmpContentLogo.test_en_template_style_function_modify_tmp_content_logo(self)
#tested but not fully verified.
class EnTemplateStyleFunctionModifyTmpContentTouchNontouch(TestCase6.EnTemplateStyleFunctionModifyTmpContentTouchNontouch):
    def test_en_template_style_function_modify_tmp_content_touch_nontouch(self):
        TestCase6.EnTemplateStyleFunctionModifyTmpContentTouchNontouch.test_en_template_style_function_modify_tmp_content_touch_nontouch(self)

class EnTemplateStyleFunctionModifyTmpName(TestCase7.EnTemplateStyleFunctionModifyTmpName):
    def test_en_template_style_function_modify_tmp_name(self):
        TestCase7.EnTemplateStyleFunctionModifyTmpName.test_en_template_style_function_modify_tmp_name(self)

class EnTemplateStyleFunctionSearch(TestCase8.EnTemplateStyleFunctionSearch):
    def test_en_template_style_function_search(self):
        TestCase8.EnTemplateStyleFunctionSearch.test_en_template_style_function_search(self)

    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnTemplateStyleContentVerification("test_en_template_style_content_verification"))
    testsuite.addTest(EnTemplateStyleContentVerificationHelp("test_en_template_style_content_verification_help"))
    testsuite.addTest(EnTemplateStyleFunctionCreateTemplates("test_en_template_style_function_create_templates"))
    testsuite.addTest(EnTemplateStyleFunctionDuplicateTmp("test_en_template_style_function_duplicate_tmp"))
    testsuite.addTest(EnTemplateStyleFunctionModifyTmpContentLogo("test_en_template_style_function_modify_tmp_content_logo"))
    testsuite.addTest(EnTemplateStyleFunctionModifyTmpContentTouchNontouch("test_en_template_style_function_modify_tmp_content_touch_nontouch"))
    testsuite.addTest(EnTemplateStyleFunctionModifyTmpName("test_en_template_style_function_modify_tmp_name"))
    testsuite.addTest(EnTemplateStyleFunctionSearch("test_en_template_style_function_search"))


    filename = gb_filename_prefix+'/TemplateStyle.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Template Styles',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)