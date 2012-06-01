# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#import HTMLTestRunner
from Webdriver.HTMLTestRunner import *
from Webdriver.all_globals import *
from Webdriver.testCase.functionalTesting.login import languageSelection as loginCase1
from Webdriver.testCase.functionalTesting.login import languageSelection_en as loginCase2
from Webdriver.testCase.functionalTesting.login import languageSelection_de as loginCase3
from Webdriver.testCase.functionalTesting.login import languageSelection_es as loginCase4
from Webdriver.testCase.functionalTesting.login import languageSelection_fr as loginCase5
from Webdriver.testCase.functionalTesting.login import languageSelection_it as loginCase6
from Webdriver.testCase.functionalTesting.login import languageSelection_ja as loginCase7
from Webdriver.testCase.functionalTesting.login import languageSelection_nl as loginCase8
from Webdriver.testCase.functionalTesting.login import languageSelection_pt as loginCase9
from Webdriver.testCase.functionalTesting.login import languageSelection_ru as loginCase10
from Webdriver.testCase.functionalTesting.login import languageSelection_tr as loginCase11
from Webdriver.testCase.functionalTesting.login import languageSelection_zh as loginCase12


def setUp(self):
    gb_setUp(self)

class LoginLanguageSelection(loginCase1.LanguageSelection):
    
    def test_login_language_selection(self):
        loginCase1.LanguageSelection.test_login_language_selection(self)

#Verify Element for different languages.        
#Verify Element for en
class LoginLanguageSelectionEn(loginCase2.LoginLanguageSelectionEn):
    def test_login_language_selection_en(self):
        loginCase2.LoginLanguageSelectionEn.test_login_language_selection_en(self)

#Verify Element for de
class LoginLanguageSelectionDe(loginCase3.LoginLanguageSelectionDe):
    def test_login_language_selection_de(self):
        loginCase3.LoginLanguageSelectionDe.test_login_language_selection_de(self)

#Verify Element for es
class LoginLanguageSelectionEs(loginCase4.LoginLanguageSelectionEs):
    def test_login_language_selection_es(self):
        loginCase4.LoginLanguageSelectionEs.test_login_language_selection_es(self)
        
#Verify Element for fr
class LoginLanguageSelectionFr(loginCase5.LoginLanguageSelectionFr):
    def test_login_language_selection_fr(self):
        loginCase5.LoginLanguageSelectionFr.test_login_language_selection_fr(self)

#Verify Element for it
class LoginLanguageSelectionIt(loginCase6.LoginLanguageSelectionIt):
    def test_login_language_selection_it(self):
        loginCase6.LoginLanguageSelectionIt.test_login_language_selection_it(self)

#Verify Element for ja
class LoginLanguageSelectionJa(loginCase7.LoginLanguageSelectionJa):
    def test_login_language_selection_ja(self):
        loginCase7.LoginLanguageSelectionJa.test_login_language_selection_ja(self)

#Verify Element for nl
class LoginLanguageSelectionNl(loginCase8.LoginLanguageSelectionNl):
    def test_login_language_selection_nl(self):
        loginCase8.LoginLanguageSelectionNl.test_login_language_selection_nl(self)

#Verify Element for pt
class LoginLanguageSelectionPt(loginCase9.LoginLanguageSelectionPt):
    def test_login_language_selection_pt(self):
        loginCase9.LoginLanguageSelectionPt.test_login_language_selection_pt(self)

#Verify Element for ru
class LoginLanguageSelectionRu(loginCase10.LoginLanguageSelectionRu):
    def test_login_language_selection_ru(self):
        loginCase10.LoginLanguageSelectionRu.test_login_language_selection_ru(self)

#Verify Element for tr
class LoginLanguageSelectionTr(loginCase11.LoginLanguageSelectionTr):
    def test_login_language_selection_tr(self):
        loginCase11.LoginLanguageSelectionTr.test_login_language_selection_tr(self)

#Verify Element for zh
class LoginLanguageSelectionZh(loginCase12.LoginLanguageSelectionZh):
    def test_login_language_selection_zh(self):
        loginCase12.LoginLanguageSelectionZh.test_login_language_selection_zh(self)

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(LoginLanguageSelection("test_login_language_selection"))
    testsuite.addTest(LoginLanguageSelectionEn("test_login_language_selection_en"))
    testsuite.addTest(LoginLanguageSelectionDe("test_login_language_selection_de"))
    testsuite.addTest(LoginLanguageSelectionEs("test_login_language_selection_es"))
    testsuite.addTest(LoginLanguageSelectionFr("test_login_language_selection_fr"))
    testsuite.addTest(LoginLanguageSelectionIt("test_login_language_selection_it"))
    testsuite.addTest(LoginLanguageSelectionJa("test_login_language_selection_ja"))
    testsuite.addTest(LoginLanguageSelectionNl("test_login_language_selection_nl"))
    testsuite.addTest(LoginLanguageSelectionPt("test_login_language_selection_pt"))
    testsuite.addTest(LoginLanguageSelectionRu("test_login_language_selection_ru"))
    testsuite.addTest(LoginLanguageSelectionTr("test_login_language_selection_tr"))
    testsuite.addTest(LoginLanguageSelectionZh("test_login_language_selection_zh"))

    filename = gb_filename_prefix+'/languageSelection.html'
    #filename = '/home/zignage/EV-SeleniumTest/WebDriver/result/languageSelection.html'
    fp = file(filename,'wb')

#    runner = HTMLTestRunner.HTMLTestRunner(
    runner = HTMLTestRunner(
            stream=fp,
            title='Test Result',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
