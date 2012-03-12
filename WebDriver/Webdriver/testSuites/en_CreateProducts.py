#1)Content Verification
#2)Create/delete/modify manufacture
#3)Create products
#4)Search function for media
#5)Search function for products
#6)Drag and Drop function is pending
#7)Upload media function is pending.
#8)Delete the product once finish testing.
#note: delete the product '' manually after testing.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
##from WebDriver.testCase.BaseTestCase import BaseTestCase
import unittest, time, re
import HTMLTestRunner
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_Function_CreateManufacture as TestCase3
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_Function_CreateProducts as TestCase4
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_Function_MediaSearch as TestCase5
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_Function_ProductSearch as TestCase6
from Webdriver.testCase.functionalTesting.CreateProducts import en_CreateProducts_Function_UploadMedia as TestCase7

def setUp(self):
    gb_setUp(self)

class EnCreateProductsContentVerification(TestCase1.EnCreateProductsContentVerification):
    def test_en_create_products_content_verification(self):
        TestCase1.EnCreateProductsContentVerification.test_en_create_products_content_verification(self)
    
class EnCreateProductsContentVerificationHelp(TestCase2.EnCreateProductsContentVerificationHelp):
    def test_en_create_products_content_verification_help(self):
        TestCase2.EnCreateProductsContentVerificationHelp.test_en_create_products_content_verification_help(self)

class EnCreateProductsFunctionCreateManufacture(TestCase3.EnCreateProductsFunctionCreateManufacture):
    def test_en_create_products_function_create_manufacture(self):
        TestCase3.EnCreateProductsFunctionCreateManufacture.test_en_create_products_function_create_manufacture(self)

class EnCreateProductsFunctionCreateProducts(TestCase4.EnCreateProductsFunctionCreateProducts):
    def test_en_create_products_function_create_products(self):
        TestCase4.EnCreateProductsFunctionCreateProducts.test_en_create_products_function_create_products(self)

class EnCreateProductsFunctionMediaSearch(TestCase5.EnCreateProductsFunctionMediaSearch):
    def test_en_create_products_function_media_search(self):
        TestCase5.EnCreateProductsFunctionMediaSearch.test_en_create_products_function_media_search(self)

class EnCreateProductsFunctionProductSearch(TestCase6.EnCreateProductsFunctionProductSearch):
    def test_en_create_products_function_product_search(self):
        TestCase6.EnCreateProductsFunctionProductSearch.test_en_create_products_function_product_search(self)

#This one is pending.
class EnCreateProductsFunctionUploadMedia(TestCase7.EnCreateProductsFunctionUploadMedia):
    def test_en_create_products_function_upload_media(self):
        TestCase7.EnCreateProductsFunctionUploadMedia.test_en_create_products_function_upload_media(self)

    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnCreateProductsContentVerification("test_en_create_products_content_verification"))
    testsuite.addTest(EnCreateProductsContentVerificationHelp("test_en_create_products_content_verification_help"))
    testsuite.addTest(EnCreateProductsFunctionCreateManufacture("test_en_create_products_function_create_manufacture"))
    testsuite.addTest(EnCreateProductsFunctionCreateProducts("test_en_create_products_function_create_products"))
    testsuite.addTest(EnCreateProductsFunctionMediaSearch("test_en_create_products_function_media_search"))
    testsuite.addTest(EnCreateProductsFunctionProductSearch("test_en_create_products_function_product_search"))
    testsuite.addTest(EnCreateProductsFunctionUploadMedia("test_en_create_products_function_upload_media"))
    filename = gb_filename_prefix+'/CreateProducts.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
