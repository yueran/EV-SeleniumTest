from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.HTMLTestRunner import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_Function_DragAndDrop as TestCase3
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_Function_CategoryOption as TestCase4
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_Function_SubCategoryOption as TestCase5
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_Function_KeywordOption as TestCase6
from Webdriver.testCase.functionalTesting.ClassifyProduct import en_ClassifyProducts_Function_addElement as TestCase7

def setUp(self):
    gb_setUp(self)

class EnClassifyProductsContentVerification(TestCase1.EnClassifyProductsContentVerification):
    
    def test_en_classify_products_content_verification(self):
        TestCase1.EnClassifyProductsContentVerification.test_en_classify_products_content_verification(self)

class EnClassifyProductsContentVerificationHelp(TestCase2.EnClassifyProductsContentVerificationHelp):

    def test_en_classify_products_content_verification_help(self):
        TestCase2.EnClassifyProductsContentVerificationHelp.test_en_classify_products_content_verification_help(self)

class EnClassifyProductsFunctionDragAndDrop(TestCase3.EnClassifyProductsFunctionDragAndDrop):

    def test_en_classify_products_function_drag_and_drop(self):
        TestCase3.EnClassifyProductsFunctionDragAndDrop.test_en_classify_products_function_drag_and_drop(self)

class EnClassifyProductsFunctionCategoryOption(TestCase4.EnClassifyProductsFunctionCategoryOption):

    def test_en_classify_products_function_category_option(self):
        TestCase4.EnClassifyProductsFunctionCategoryOption.test_en_classify_products_function_category_option(self)

class EnClassifyProductsFunctionSubCategoryOption(TestCase5.EnClassifyProductsFunctionSubCategoryOption):

    def test_en_classify_products_function_sub_option(self):
        TestCase5.EnClassifyProductsFunctionSubCategoryOption.test_en_classify_products_function_sub_option(self)

class EnClassifyProductsFunctionKeywordOption(TestCase6.EnClassifyProductsFunctionKeywordOption):

    def test_en_classify_products_function_keyword_option(self):
        TestCase6.EnClassifyProductsFunctionKeywordOption.test_en_classify_products_function_keyword_option(self)

class EnClassifyProductsFunctionAddElement(TestCase7.EnClassifyProductsFunctionAddElement):

    def test_en_classify_products_function_add_element(self):
        TestCase7.EnClassifyProductsFunctionAddElement.test_en_classify_products_function_add_element(self)

        
    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnClassifyProductsContentVerification("test_en_classify_products_content_verification"))
    testsuite.addTest(EnClassifyProductsContentVerificationHelp("test_en_classify_products_content_verification_help"))
    testsuite.addTest(EnClassifyProductsFunctionDragAndDrop("test_en_classify_products_function_drag_and_drop"))
    testsuite.addTest(EnClassifyProductsFunctionCategoryOption("test_en_classify_products_function_category_option"))
    testsuite.addTest(EnClassifyProductsFunctionSubCategoryOption("test_en_classify_products_function_sub_option"))
    testsuite.addTest(EnClassifyProductsFunctionKeywordOption("test_en_classify_products_function_keyword_option"))
    testsuite.addTest(EnClassifyProductsFunctionAddElement("test_en_classify_products_function_add_element"))


    filename = gb_filename_prefix+'/ClassifyProducts.html'
    fp = file(filename,'wb')

#    runner = HTMLTestRunner.HTMLTestRunner(
    runner =HTMLTestRunner(
            stream=fp,
            title='Classify Products',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
    
#if __name__ == "__main__":
#    unittest.main()
