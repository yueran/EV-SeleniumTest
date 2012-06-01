from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.HTMLTestRunner import *
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testCase.functionalTesting.addProductToPosts import en_AddProductsToPosts_Verification as TestCase1
from Webdriver.testCase.functionalTesting.addProductToPosts import en_AddProductsToPosts_Verification_Help as TestCase2
from Webdriver.testCase.functionalTesting.addProductToPosts import en_AddProductsToPosts_Search as TestCase3


def setUp(self):
    gb_setUp(self)
    
class EnAddProductsToPostsVerification(TestCase1.EnAddProductsToPostsVerification):

    def test_en_add_products_to_posts_verification(self):
        TestCase1.EnAddProductsToPostsVerification.test_en_add_products_to_posts_verification(self)

class EnAddProductsToPostsHelp(TestCase2.EnAddProductsToPostsHelp):
    def test_en_add_products_to_posts_help(self):
        TestCase2.EnAddProductsToPostsHelp.test_en_add_products_to_posts_help(self)

class EnAddProductsToPostsSearch(TestCase3.EnAddProductsToPostsSearch):

    def test_en_add_products_to_posts_search(self):
        TestCase3.EnAddProductsToPostsSearch.test_en_add_products_to_posts_search(self)
    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnAddProductsToPostsVerification("test_en_add_products_to_posts_verification"))
    testsuite.addTest(EnAddProductsToPostsHelp("test_en_add_products_to_posts_help"))
    testsuite.addTest(EnAddProductsToPostsSearch("test_en_add_products_to_posts_search"))


    filename = gb_filename_prefix+'/AddProductsToPosts.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)

#if __name__ == "__main__":
#    unittest.main()
