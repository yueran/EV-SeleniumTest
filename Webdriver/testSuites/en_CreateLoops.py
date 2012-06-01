#Note: Need to manually delete loop with name 'new attract loop' after testing!!
#Upload media , drag and drop and seq no(TestCase4, TestCase8 and TestCase9) have not been fully implemented yet~!
from selenium.common.exceptions import NoSuchElementException
#import HTMLTestRunner
from Webdriver.all_globals import *
from Webdriver.HTMLTestRunner import *
from Webdriver.contentMaintenance import *

from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_ContentVerification_Help as TestCase2
#from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_CreateNewLoop as TestCase3
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_DragAndDrop as TestCase4
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_EditLoopName as TestCase5
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_Preview as TestCase6
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_Search as TestCase7
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_SequenceNo as TestCase8
from Webdriver.testCase.functionalTesting.createLoops import en_CreateLoops_Function_UploadNewVideo as TestCase9


def setUp(self):
    gb_setUp(self)

class EnCreateLoopsContentVerification(TestCase1.EnCreateLoopsContentVerification):
    def test_en_create_loops_content_verification(self):
        TestCase1.EnCreateLoopsContentVerification.test_en_create_loops_content_verification(self)

class EnCreateLoopsContentVerificationHelp(TestCase2.EnCreateLoopsContentVerificationHelp):
    def test_en_create_loops_content_verification_help(self):
        TestCase2.EnCreateLoopsContentVerificationHelp.test_en_create_loops_content_verification_help(self)

#class EnCreateLoopsFunctionCreateNewLoop(TestCase3.EnCreateLoopsFunctionCreateNewLoop):
#	def test_en_create_loops_function_create_new_loop(self):
#		TestCase3.EnCreateLoopsFunctionCreateNewLoop.test_en_create_loops_function_create_new_loop(self)

class EnCreateLoopsFunctionDragAndDrop(TestCase4.EnCreateLoopsFunctionDragAndDrop):
	def test_en_create_loops_function_drag_and_drop(self):
		TestCase4.EnCreateLoopsFunctionDragAndDrop.test_en_create_loops_function_drag_and_drop(self)

class EnCreateLoopsFunctionEditLoopNameAndCreateLoops(TestCase5.EnCreateLoopsFunctionEditLoopNameAndCreateLoops):
	def test_en_create_loops_function_edit_loop_name_and_create_loops(self):
		TestCase5.EnCreateLoopsFunctionEditLoopNameAndCreateLoops.test_en_create_loops_function_edit_loop_name_and_create_loops(self)

class EnCreateLoopsFunctionPreview(TestCase6.EnCreateLoopsFunctionPreview):
	def test_en_create_loops_function_preview(self):
		TestCase6.EnCreateLoopsFunctionPreview.test_en_create_loops_function_preview(self)

class EnCreateLoopsFunctionSearch(TestCase7.EnCreateLoopsFunctionSearch):
	def test_en_create_loops_function_search(self):
		TestCase7.EnCreateLoopsFunctionSearch.test_en_create_loops_function_search(self)

class EnCreateLoopsFunctionSequenceNo(TestCase8.EnCreateLoopsFunctionSequenceNo):
	def test_en_create_loops_function_sequence_no(self):
		TestCase8.EnCreateLoopsFunctionSequenceNo.test_en_create_loops_function_sequence_no(self)

class EnCreateLoopsFunctionUploadNewVideo(TestCase9.EnCreateLoopsFunctionUploadNewVideo):
	def test_en_create_loops_function_upload_new_video(self):
		TestCase9.EnCreateLoopsFunctionUploadNewVideo.test_en_create_loops_function_upload_new_video(self)


def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True

def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnCreateLoopsContentVerification("test_en_create_loops_content_verification"))
    testsuite.addTest(EnCreateLoopsContentVerificationHelp("test_en_create_loops_content_verification_help"))
#    testsuite.addTest(EnCreateLoopsFunctionCreateNewLoop("test_en_create_loops_function_create_new_loop"))
    testsuite.addTest(EnCreateLoopsFunctionDragAndDrop("test_en_create_loops_function_drag_and_drop"))
    testsuite.addTest(EnCreateLoopsFunctionEditLoopNameAndCreateLoops("test_en_create_loops_function_edit_loop_name_and_create_loops"))
    testsuite.addTest(EnCreateLoopsFunctionPreview("test_en_create_loops_function_preview"))
    testsuite.addTest(EnCreateLoopsFunctionSearch("test_en_create_loops_function_search"))
    testsuite.addTest(EnCreateLoopsFunctionSequenceNo("test_en_create_loops_function_sequence_no"))
    testsuite.addTest(EnCreateLoopsFunctionUploadNewVideo("test_en_create_loops_function_upload_new_video"))


    filename = gb_filename_prefix+'/CreateLoops.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Create Loops'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
