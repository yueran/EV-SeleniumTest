from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.HTMLTestRunner import *
from selenium.webdriver import ActionChains

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

    runner = HTMLTestRunner(
            stream=fp,
            title='Create Products',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)


#if __name__ == "__main__":
#    unittest.main()
