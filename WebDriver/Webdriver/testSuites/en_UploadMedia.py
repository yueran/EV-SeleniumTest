#This test suites contains following aspects:
#1)Contention Verification: This is to test if all the elements are in that page and no picture etc missing.
#2)Test the content for 'Help' is complete;
#3)Test the add element function(create media group)
#4)Test the function of modifying the name of mediagroup and media
#5)Test the Drag And Drop function
#6)Test the search function
#7)Please note: *Deleting testing is not been implemented in this test. After testing, please delete the newly created items.
#               *Search function testing is not fully implemented here.
#               *Drag and drop test pass but there might be some problem with the testing case.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_Function_CreateMedia as TestCase3
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_Function_DragAndDrop as TestCase4
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_Function_MediaGroup as TestCase5
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_Function_ModifyMedia as TestCase6
from Webdriver.testCase.functionalTesting.UploadMedia import en_UploadMedia_Function_Search as TestCase7

def setUp(self):
        gb_setUp(self)

class EnUploadMediaContentVerification(TestCase1.EnUploadMediaContentVerification):
    def test_en_upload_media_content_verification(self):
        TestCase1.EnUploadMediaContentVerification.test_en_upload_media_content_verification(self)

class EnUploadMediaContentVerificationHelp(TestCase2.EnUploadMediaContentVerificationHelp):
    def test_en_upload_media_content_verification_help(self):
        TestCase2.EnUploadMediaContentVerificationHelp.test_en_upload_media_content_verification_help(self)

#Note: This one is pending because I have not figure out how to test upload a media from local folder.
class EnUploadMediaFunctionCreateMedia(TestCase3.EnUploadMediaFunctionCreateMedia):
    def test_en_upload_media_function_create_media(self):
        TestCase3.EnUploadMediaFunctionCreateMedia.test_en_upload_media_function_create_media(self)

#Drag and drop function test pass, but there might be some problem with the test case.
class EnUploadMediaFunctionDragAndDrop(TestCase4.EnUploadMediaFunctionDragAndDrop):
    def test_en_upload_media_function_drag_and_drop(self):
        TestCase4.EnUploadMediaFunctionDragAndDrop.test_en_upload_media_function_drag_and_drop(self)
#Need to delete the media group 'CreateMediaGroup' manually after testing.
class EnUploadMediaFunctionMediaGroup(TestCase5.EnUploadMediaFunctionMediaGroup):
    def test_en_upload_media_function_media_group(self):
        TestCase5.EnUploadMediaFunctionMediaGroup.test_en_upload_media_function_media_group(self)

class EnUploadMediaFunctionModifyMedia(TestCase6.EnUploadMediaFunctionModifyMedia):
    def test_en_upload_media_function_modify_media(self):
        TestCase6.EnUploadMediaFunctionModifyMedia.test_en_upload_media_function_modify_media(self)

class EnUploadMediaFunctionSearch(TestCase7.EnUploadMediaFunctionSearch):
    def test_en_upload_media_function_search(self):
        TestCase7.EnUploadMediaFunctionSearch.test_en_upload_media_function_search(self)

    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnUploadMediaContentVerification("test_en_upload_media_content_verification"))
    testsuite.addTest(EnUploadMediaContentVerificationHelp("test_en_upload_media_content_verification_help"))
    testsuite.addTest(EnUploadMediaFunctionCreateMedia("test_en_upload_media_function_create_media"))
    testsuite.addTest(EnUploadMediaFunctionDragAndDrop("test_en_upload_media_function_drag_and_drop"))
    testsuite.addTest(EnUploadMediaFunctionMediaGroup("test_en_upload_media_function_media_group"))
    testsuite.addTest(EnUploadMediaFunctionModifyMedia("test_en_upload_media_function_modify_media"))
    testsuite.addTest(EnUploadMediaFunctionSearch("test_en_upload_media_function_search"))
    filename = gb_filename_prefix+'/UploadMedia.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
