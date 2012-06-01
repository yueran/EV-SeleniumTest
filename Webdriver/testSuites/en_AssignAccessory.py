#Test case1: contentVerification
#Test case2: helpe content verification
#Test case3:assign product(Not fully implemented)
#Test case4:search function for accessory and product.
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#import HTMLTestRunner
from Webdriver.contentMaintenance import *
from Webdriver.HTMLTestRunner import *
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.AssignAccessory import en_AssignAccessory_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.AssignAccessory import en_AssignAccessory_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.AssignAccessory import en_AssignAccessory_Function_Assign as TestCase3
from Webdriver.testCase.functionalTesting.AssignAccessory import en_AssignAccessory_Function_Search as TestCase4

def setUp(self):
    gb_setUp(self)

#Test Case1: content verification:
class EnAssignAccessoryContentVerification(TestCase1.EnAssignAccessoryContentVerification):
    def test_en_assign_accessory_content_verification(self):
        TestCase1.EnAssignAccessoryContentVerification.test_en_assign_accessory_content_verification(self)

#Test Case2: Help content verification:
class EnAssignAccessoryContentVerificationHelp(TestCase2.EnAssignAccessoryContentVerificationHelp):
    def test_en_assign_accessory_content_verification_help(self):
        TestCase2.EnAssignAccessoryContentVerificationHelp.test_en_assign_accessory_content_verification_help(self)

#Test Case3: assign/unassign function
#note: this test case still has some problem
class EnAssignAccessoryFunctionAssign(TestCase3.EnAssignAccessoryFunctionAssign):
    def test_en_assign_accessory_function_assign(self):
        TestCase3.EnAssignAccessoryFunctionAssign.test_en_assign_accessory_function_assign(self)

#Test Case4: Search function
class EnAssignAccessoryFunctionSearch(TestCase4.EnAssignAccessoryFunctionSearch):
    def test_en_assign_accessory_function_search(self):
        TestCase4.EnAssignAccessoryFunctionSearch.test_en_assign_accessory_function_search(self)
    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnAssignAccessoryContentVerification("test_en_assign_accessory_content_verification"))
    testsuite.addTest(EnAssignAccessoryContentVerificationHelp("test_en_assign_accessory_content_verification_help"))
    testsuite.addTest(EnAssignAccessoryFunctionAssign("test_en_assign_accessory_function_assign"))
    testsuite.addTest(EnAssignAccessoryFunctionSearch("test_en_assign_accessory_function_search"))


    filename = gb_filename_prefix+'/AssignAccessory.html'
    fp = file(filename,'wb')

    runner =HTMLTestRunner(
            stream=fp,
            title='Assign Accessory',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
