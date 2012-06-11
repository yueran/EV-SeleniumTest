from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import HTMLTestRunner
from Webdriver.HTMLTestRunner import *
from Webdriver.contentMaintenance import *
from Webdriver.all_globals import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
from Webdriver.testCase.functionalTesting.StoreHierarchy import en_StoreHierarchy_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.StoreHierarchy import en_StoreHierarchy_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.StoreHierarchy import en_StoreHierarchy_Function_Create as TestCase3
from Webdriver.testCase.functionalTesting.StoreHierarchy import en_StoreHierarchy_Function_DragAndDrop as TestCase4
from Webdriver.testCase.functionalTesting.StoreHierarchy import en_StoreHierarchy_Function_Duplication as TestCase5
from Webdriver.testCase.functionalTesting.StoreHierarchy import en_StoreHierarchy_Function_Modification as TestCase6

#Need to delete newly created items names 'newxxx' and '--copy(1)' after testing.
def setUp(self):
    gb_setUp(self)
    
class EnStoreHierarchyContentVerification(TestCase1.EnStoreHierarchyContentVerification):
    def test_en_store_hierarchy_content_verification(self):
        TestCase1.EnStoreHierarchyContentVerification.test_en_store_hierarchy_content_verification(self)

class EnStoreHierarchyHelpContentVerification(TestCase2.EnStoreHierarchyHelpContentVerification):
    def test_en_store_hierarchy_content_verification_help(self):
        TestCase2.EnStoreHierarchyHelpContentVerification.test_en_store_hierarchy_content_verification_help(self)
        
class EnStoreHierarchyFunctionCreate(TestCase3.EnStoreHierarchyFunctionCreate):
    def test_en_store_hierarchy_function_create(self):
        TestCase3.EnStoreHierarchyFunctionCreate.test_en_store_hierarchy_function_create(self)

#not fully implemented
class EnStoreHierarchyFunctionDragAndDrop(TestCase4.EnStoreHierarchyFunctionDragAndDrop):
    def test_en_store_hierarchy_function_drag_and_drop(self):
        TestCase4.EnStoreHierarchyFunctionDragAndDrop.test_en_store_hierarchy_function_drag_and_drop(self)
#False negative. Check it manually
class EnStoreHierarchyFunctionDuplication(TestCase5.EnStoreHierarchyFunctionDuplication):
    def test_en_store_hierarchy_function_duplication(self):
        TestCase5.EnStoreHierarchyFunctionDuplication.test_en_store_hierarchy_function_duplication(self)

class EnStoreHierarchyFunctionModification(TestCase6.EnStoreHierarchyFunctionModification):
    def test_en_store_hierarchy_function_modification(self):
        TestCase6.EnStoreHierarchyFunctionModification.test_en_store_hierarchy_function_modification(self)

    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnStoreHierarchyContentVerification("test_en_store_hierarchy_content_verification"))
    testsuite.addTest(EnStoreHierarchyHelpContentVerification("test_en_store_hierarchy_content_verification_help"))
    testsuite.addTest(EnStoreHierarchyFunctionCreate("test_en_store_hierarchy_function_create"))
    testsuite.addTest(EnStoreHierarchyFunctionDragAndDrop("test_en_store_hierarchy_function_drag_and_drop"))
    testsuite.addTest(EnStoreHierarchyFunctionDuplication("test_en_store_hierarchy_function_duplication"))
    testsuite.addTest(EnStoreHierarchyFunctionModification("test_en_store_hierarchy_function_modification"))


    filename = gb_filename_prefix+'/StoreHierarchy.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
