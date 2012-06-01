#Issues that been tested:
#1)Content verification:
#2)LockUnclock function
#3)Reset password
#4)Search function.


from selenium.common.exceptions import NoSuchElementException
#import HTMLTestRunner
from Webdriver.HTMLTestRunner import *
from Webdriver.contentMaintenance import *
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.viewNetworkStatus import en_ViewNetworkStatus_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.viewNetworkStatus import en_ViewNetworkStatus_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.viewNetworkStatus import en_ViewNetworkStatus_Function_LockUnlock as TestCase3
from Webdriver.testCase.functionalTesting.viewNetworkStatus import en_ViewNetworkStatus_Function_ResetPwd as TestCase4
from Webdriver.testCase.functionalTesting.viewNetworkStatus import en_ViewNetworkStatus_Function_Search as TestCase5

def setUp(self):
    gb_setUp(self)
	
class EnViewNetworkStatusContentVerification(TestCase1.EnViewNetworkStatusContentVerification):
    
    def test_en_view_network_status_content_verification(self):
		TestCase1.EnViewNetworkStatusContentVerification.test_en_view_network_status_content_verification(self)

class EnViewNetworkStatusContentVerificationHelp(TestCase2.EnViewNetworkStatusContentVerificationHelp):
    def test_en_view_network_status_content_verification_help(self):
		TestCase2.EnViewNetworkStatusContentVerificationHelp.test_en_view_network_status_content_verification_help(self)

class EnViewNetworkStatusFunctionLockUnlock(TestCase3.EnViewNetworkStatusFunctionLockUnlock):
	def test_en_view_network_status_function_lock_unlock(self):
		TestCase3.EnViewNetworkStatusFunctionLockUnlock.test_en_view_network_status_function_lock_unlock(self)
		
class EnViewNetworkStatusFunctionResetPwd(TestCase4.EnViewNetworkStatusFunctionResetPwd):
	def test_en_view_network_status_function_reset_pwd(self):
		TestCase4.EnViewNetworkStatusFunctionResetPwd.test_en_view_network_status_function_reset_pwd(self)

class EnViewNetworkStatusFunctionSearch(TestCase5.EnViewNetworkStatusFunctionSearch):
    def test_en_view_network_status_function_search(self):
		TestCase5.EnViewNetworkStatusFunctionSearch.test_en_view_network_status_function_search(self)



def is_element_present(self, how, what):
	try: self.driver.find_element(by=how, value=what)
	except NoSuchElementException, e: return False
	return True
    
def tearDown(self):
	self.driver.quit()
	self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnViewNetworkStatusContentVerification("test_en_view_network_status_content_verification"))
    testsuite.addTest(EnViewNetworkStatusContentVerificationHelp("test_en_view_network_status_content_verification_help"))
    testsuite.addTest(EnViewNetworkStatusFunctionLockUnlock("test_en_view_network_status_function_lock_unlock"))
    testsuite.addTest(EnViewNetworkStatusFunctionResetPwd("test_en_view_network_status_function_reset_pwd"))
    testsuite.addTest(EnViewNetworkStatusFunctionSearch("test_en_view_network_status_function_search"))

    filename = gb_filename_prefix+'/ViewNetworkStatus.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='View Network Status'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
