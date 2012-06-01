#Issues that been tested:
#1)Content verification:
#2)EditTemplateName
#3)EditTemplateSchedule(Partically)
#4)Search function.
#5)Note: Drag and Drop function testing is pending.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.HTMLTestRunner import *
from Webdriver.contentMaintenance import *
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_Function_DragAndDrop as TestCase3
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_Function_EditTempName as TestCase4
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_Function_EditTempSchedule as TestCase5
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_Function_EditTempSchedule2 as TestCase6
from Webdriver.testCase.functionalTesting.scheduleTemplates import en_ScheduleTemplates_Function_Search as TestCase7

def setUp(self):
    gb_setUp(self)
	
class EnScheduleTemplatesContentVerification(TestCase1.EnScheduleTemplatesContentVerification):
    
    def test_en_schedule_templates_content_verification(self):
		TestCase1.EnScheduleTemplatesContentVerification.test_en_schedule_templates_content_verification(self)

class EnScheduleTemplatesContentVerificationHelp(TestCase2.EnScheduleTemplatesContentVerificationHelp):
    def test_en_schedule_templates_content_verification_help(self):
		TestCase2.EnScheduleTemplatesContentVerificationHelp.test_en_schedule_templates_content_verification_help(self)

#Drag and drop not implemented yet.
class EnScheduleTemplatesFunctionDragAndDrop(TestCase3.EnScheduleTemplatesFunctionDragAndDrop):
	def test_en_schedule_templates_function_drag_and_drop(self):
		TestCase3.EnScheduleTemplatesFunctionDragAndDrop.test_en_schedule_templates_function_drag_and_drop(self)
		
class EnScheduleTemplatesFunctionEditTempName(TestCase4.EnScheduleTemplatesFunctionEditTempName):
	def test_en_schedule_templates_function_edit_temp_name(self):
		TestCase4.EnScheduleTemplatesFunctionEditTempName.test_en_schedule_templates_function_edit_temp_name(self)

class EnScheduleTemplatesFunctionEditTempSchedule1(TestCase5.EnScheduleTemplatesFunctionEditTempSchedule1):
    def test_en_schedule_templates_function_edit_temp_schedule1(self):
		TestCase5.EnScheduleTemplatesFunctionEditTempSchedule1.test_en_schedule_templates_function_edit_temp_schedule1(self)

class EnScheduleTemplatesFunctionEditTempSchedule2(TestCase6.EnScheduleTemplatesFunctionEditTempSchedule2):
	def test_en_schedule_templates_function_edit_temp_schedule2(self):
		TestCase6.EnScheduleTemplatesFunctionEditTempSchedule2.test_en_schedule_templates_function_edit_temp_schedule2(self)

class EnScheduleTemplatesFunctionSearch(TestCase7.EnScheduleTemplatesFunctionSearch):
	def test_en_schedule_templates_function_search(self):
		TestCase7.EnScheduleTemplatesFunctionSearch.test_en_schedule_templates_function_search(self)


def is_element_present(self, how, what):
	try: self.driver.find_element(by=how, value=what)
	except NoSuchElementException, e: return False
	return True
    
def tearDown(self):
	self.driver.quit()
	self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnScheduleTemplatesContentVerification("test_en_schedule_templates_content_verification"))
    testsuite.addTest(EnScheduleTemplatesContentVerificationHelp("test_en_schedule_templates_content_verification_help"))
    testsuite.addTest(EnScheduleTemplatesFunctionDragAndDrop("test_en_schedule_templates_function_drag_and_drop"))
    testsuite.addTest(EnScheduleTemplatesFunctionEditTempName("test_en_schedule_templates_function_edit_temp_name"))
    testsuite.addTest(EnScheduleTemplatesFunctionEditTempSchedule1("test_en_schedule_templates_function_edit_temp_schedule1"))
    testsuite.addTest(EnScheduleTemplatesFunctionEditTempSchedule2("test_en_schedule_templates_function_edit_temp_schedule2"))
    testsuite.addTest(EnScheduleTemplatesFunctionSearch("test_en_schedule_templates_function_search"))
    filename = gb_filename_prefix+'/ScheduleTemplates.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Schedule Templates'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
