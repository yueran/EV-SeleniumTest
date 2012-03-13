# Before Test: Please delete user  'testtest@test.com', user group 'duplicateSuccess'
#TestCase5 now is false negative.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
import HTMLTestRunner
from selenium.webdriver import ActionChains
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUserOrGroups_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_User_Search as TestCase3
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_AssignUassignUserGroup as TestCase4
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_ChangePermissions_AssignAccessories as TestCase5
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_CreateGroups as TestCase6
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_DuplicateGroups as TestCase7
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_EditGroups as TestCase8
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_UsersGroups_PermissionNames as TestCase9
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_Users_CreateUsers as TestCase10
from Webdriver.testCase.functionalTesting.setupUsersOrGroups import en_SetupUsersOrGroups_Function_Users_EditUsers as TestCase11


def setUp(self):
    gb_setUp(self)

class EnSetupUsersOrGroupsContentVerification(TestCase1.EnSetupUsersOrGroupsContentVerification):
    def test_en_setup_users_or_groups_content_verification(self):
        TestCase1.EnSetupUsersOrGroupsContentVerification.test_en_setup_users_or_groups_content_verification(self)

class EnSetupUsersOrGroupsContentVerificationHelp(TestCase2.EnSetupUsersOrGroupsContentVerificationHelp):
    def test_en_setup_users_or_groups_content_verification_help(self):
        TestCase2.EnSetupUsersOrGroupsContentVerificationHelp.test_en_setup_users_or_groups_content_verification_help(self)

class EnSetupUsersOrGroupsFunctionUsersSearch(TestCase3.EnSetupUsersOrGroupsFunctionUsersSearch):
    def test_en_setup_users_or_groups_function_users_search(self):
        TestCase3.EnSetupUsersOrGroupsFunctionUsersSearch.test_en_setup_users_or_groups_function_users_search(self)
        
#Drag and drop test pass but the test case still has some problem.
class EnSetupUsersOrGroupsFunctionAssignUassignUserGroup(TestCase4.EnSetupUsersOrGroupsFunctionAssignUassignUserGroup):
    def test_en_setup_users_or_groups_function_assign_uassign_user_group(self):
        TestCase4.EnSetupUsersOrGroupsFunctionAssignUassignUserGroup.test_en_setup_users_or_groups_function_assign_uassign_user_group(self)

#This one reflect all the permission change functions.
class EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsAssignAccessories(TestCase5.EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsAssignAccessories):
    def test_en_setup_users_or_groups_function_users_groups_change_permissions_assign_accessories(self):
        TestCase5.EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsAssignAccessories.test_en_setup_users_or_groups_function_users_groups_change_permissions_assign_accessories(self)

class EnSetupUsersOrGroupsFunctionUsersGroupsCreateGroups(TestCase6.EnSetupUsersOrGroupsFunctionUsersGroupsCreateGroups):
    def test_en_setup_users_or_groups_function_users_groups_create_groups(self):
        TestCase6.EnSetupUsersOrGroupsFunctionUsersGroupsCreateGroups.test_en_setup_users_or_groups_function_users_groups_create_groups(self)

class EnSetupUsersOrGroupsFunctionUsersGroupsDuplicatedGroups(TestCase7.EnSetupUsersOrGroupsFunctionUsersGroupsDuplicatedGroups):
    def test_en_setup_users_or_groups_function_users_groups_duplicated_groups(self):
        TestCase7.EnSetupUsersOrGroupsFunctionUsersGroupsDuplicatedGroups.test_en_setup_users_or_groups_function_users_groups_duplicated_groups(self)

class EnSetupUsersOrGroupsFunctionUsersGroupsEditGroups(TestCase8.EnSetupUsersOrGroupsFunctionUsersGroupsEditGroups):
    def test_en_setup_users_or_groups_function_users_groups_edit_groups(self):
        TestCase8.EnSetupUsersOrGroupsFunctionUsersGroupsEditGroups.test_en_setup_users_or_groups_function_users_groups_edit_groups(self)

class EnSetupUsersOrGroupsFunctionUsersGroupsPermissionNames(TestCase9.EnSetupUsersOrGroupsFunctionUsersGroupsPermissionNames):
    def test_en_setup_users_or_groups_function_users_groups_permission_names(self):
        TestCase9.EnSetupUsersOrGroupsFunctionUsersGroupsPermissionNames.test_en_setup_users_or_groups_function_users_groups_permission_names(self)

class EnSetupUsersOrGroupsFunctionUsersCreateUsers(TestCase10.EnSetupUsersOrGroupsFunctionUsersCreateUsers):
    def test_en_setup_users_or_groups_function_users_create_users(self):
        TestCase10.EnSetupUsersOrGroupsFunctionUsersCreateUsers.test_en_setup_users_or_groups_function_users_create_users(self)

class EnSetupUsersOrGroupsFunctionUsersEditUsers(TestCase11.EnSetupUsersOrGroupsFunctionUsersEditUsers):
    def test_en_setup_users_or_groups_function_users_edit_users(self):
        TestCase11.EnSetupUsersOrGroupsFunctionUsersEditUsers.test_en_setup_users_or_groups_function_users_edit_users(self)

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnSetupUsersOrGroupsContentVerification("test_en_setup_users_or_groups_content_verification"))
    testsuite.addTest(EnSetupUsersOrGroupsContentVerificationHelp("test_en_setup_users_or_groups_content_verification_help"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersSearch("test_en_setup_users_or_groups_function_users_search"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionAssignUassignUserGroup("test_en_setup_users_or_groups_function_assign_uassign_user_group"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersGroupsChangePermissionsAssignAccessories("test_en_setup_users_or_groups_function_users_groups_change_permissions_assign_accessories"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersGroupsCreateGroups("test_en_setup_users_or_groups_function_users_groups_create_groups"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersGroupsDuplicatedGroups("test_en_setup_users_or_groups_function_users_groups_duplicated_groups"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersGroupsEditGroups("test_en_setup_users_or_groups_function_users_groups_edit_groups"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersGroupsPermissionNames("test_en_setup_users_or_groups_function_users_groups_permission_names"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersCreateUsers("test_en_setup_users_or_groups_function_users_create_users"))
    testsuite.addTest(EnSetupUsersOrGroupsFunctionUsersEditUsers("test_en_setup_users_or_groups_function_users_edit_users"))

    filename = gb_filename_prefix+'/SetupUsersOrGroups.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
