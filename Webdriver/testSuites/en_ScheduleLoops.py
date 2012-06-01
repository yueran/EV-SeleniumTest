#Issues that been tested:
#1)Content verification:
#2)EditLoopName
#3)EditLoopSchedule(Partically)
#4)Search function.
#5)Note: Drag and Drop function testing is pending.

from selenium.common.exceptions import NoSuchElementException
#import HTMLTestRunner
from Webdriver.HTMLTestRunner import *
from Webdriver.contentMaintenance import *
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_Function_DragAndDrop as TestCase3
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_Function_EditLoopName as TestCase4
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_Function_EditLoopSchedule as TestCase5
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_Function_EditLoopSchedule2 as TestCase6
from Webdriver.testCase.functionalTesting.scheduleLoops import en_ScheduleLoops_Function_Search as TestCase7

def setUp(self):
    gb_setUp(self)
	
class EnScheduleLoopsContentVerification(TestCase1.EnScheduleLoopsContentVerification):
    
    def test_en_schedule_loops_content_verification(self):
		TestCase1.EnScheduleLoopsContentVerification.test_en_schedule_loops_content_verification(self)

class EnScheduleLoopsContentVerificationHelp(TestCase2.EnScheduleLoopsContentVerificationHelp):
    def test_en_schedule_loops_content_verification_help(self):
		TestCase2.EnScheduleLoopsContentVerificationHelp.test_en_schedule_loops_content_verification_help(self)

#Drag and drop not implemented yet.
class EnScheduleLoopsFunctionDragAndDrop(TestCase3.EnScheduleLoopsFunctionDragAndDrop):
	def test_en_schedule_loops_function_drag_and_drop(self):
		TestCase3.EnScheduleLoopsFunctionDragAndDrop.test_en_schedule_loops_function_drag_and_drop(self)
		
class EnScheduleLoopsFunctionEditLoopName(TestCase4.EnScheduleLoopsFunctionEditLoopName):
	def test_en_schedule_loops_function_edit_loop_name(self):
		TestCase4.EnScheduleLoopsFunctionEditLoopName.test_en_schedule_loops_function_edit_loop_name(self)

class EnScheduleLoopsFunctionEditLoopSchedule1(TestCase5.EnScheduleLoopsFunctionEditLoopSchedule1):
    def test_en_schedule_loops_function_edit_loop_schedule1(self):
		TestCase5.EnScheduleLoopsFunctionEditLoopSchedule1.test_en_schedule_loops_function_edit_loop_schedule1(self)

class EnScheduleLoopsFunctionEditLoopSchedule2(TestCase6.EnScheduleLoopsFunctionEditLoopSchedule2):
	def test_en_schedule_loops_function_edit_loop_schedule2(self):
		TestCase6.EnScheduleLoopsFunctionEditLoopSchedule2.test_en_schedule_loops_function_edit_loop_schedule2(self)

class EnScheduleLoopsFunctionSearch(TestCase7.EnScheduleLoopsFunctionSearch):
	def test_en_schedule_loops_function_search(self):
		TestCase7.EnScheduleLoopsFunctionSearch.test_en_schedule_loops_function_search(self)


def is_element_present(self, how, what):
	try: self.driver.find_element(by=how, value=what)
	except NoSuchElementException, e: return False
	return True
    
def tearDown(self):
	self.driver.quit()
	self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnScheduleLoopsContentVerification("test_en_schedule_loops_content_verification"))
    testsuite.addTest(EnScheduleLoopsContentVerificationHelp("test_en_schedule_loops_content_verification_help"))
    testsuite.addTest(EnScheduleLoopsFunctionDragAndDrop("test_en_schedule_loops_function_drag_and_drop"))
    testsuite.addTest(EnScheduleLoopsFunctionEditLoopName("test_en_schedule_loops_function_edit_loop_name"))
    testsuite.addTest(EnScheduleLoopsFunctionEditLoopSchedule1("test_en_schedule_loops_function_edit_loop_schedule1"))
    testsuite.addTest(EnScheduleLoopsFunctionEditLoopSchedule2("test_en_schedule_loops_function_edit_loop_schedule2"))
    testsuite.addTest(EnScheduleLoopsFunctionSearch("test_en_schedule_loops_function_search"))
    filename = gb_filename_prefix+'/ScheduleLoops.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Schedule Loops'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
