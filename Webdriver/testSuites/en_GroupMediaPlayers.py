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
from Webdriver.testCase.functionalTesting.groupMediaPlayers import en_GroupMediaPlayers_ContentVerification as TestCase1
from Webdriver.testCase.functionalTesting.groupMediaPlayers import en_GroupMediaPlayers_ContentVerification_Help as TestCase2
from Webdriver.testCase.functionalTesting.groupMediaPlayers import en_GroupMediaPlayers_Function_DragAndDrop as TestCase3
from Webdriver.testCase.functionalTesting.groupMediaPlayers import en_GroupMediaPlayers_Function_Modification as TestCase4
from Webdriver.testCase.functionalTesting.groupMediaPlayers import en_GroupMediaPlayers_Function_Search as TestCase5


def setUp(self):
    gb_setUp(self)
    
class EnGroupMediaPlayersContentVerification(TestCase1.EnGroupMediaPlayersContentVerification):
    def test_en_group_media_players_content_verification(self):
        TestCase1.EnGroupMediaPlayersContentVerification.test_en_group_media_players_content_verification(self)

class EnGroupMediaPlayersContentVerificationHelp(TestCase2.EnGroupMediaPlayersContentVerificationHelp):
    def test_en_group_media_players_content_verification_help(self):
        TestCase2.EnGroupMediaPlayersContentVerificationHelp.test_en_group_media_players_content_verification_help(self)

class EnGroupMediaPlayersFunctionDragAndDrop(TestCase3.EnGroupMediaPlayersFunctionDragAndDrop):
    def test_en_group_media_players_function_drag_and_drop(self):
        TestCase3.EnGroupMediaPlayersFunctionDragAndDrop.test_en_group_media_players_function_drag_and_drop(self)

class EnGroupMediaPlayersFunctionModification(TestCase4.EnGroupMediaPlayersFunctionModification):
    def test_en_group_media_players_function_modification(self):
        TestCase4.EnGroupMediaPlayersFunctionModification.test_en_group_media_players_function_modification(self)

class EnGroupMediaPlayersFunctionSearch(TestCase5.EnGroupMediaPlayersFunctionSearch):
    def test_en_group_media_players_function_search(self):
        TestCase5.EnGroupMediaPlayersFunctionSearch.test_en_group_media_players_function_search(self)

    
def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
    
def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()

    testsuite.addTest(EnGroupMediaPlayersContentVerification("test_en_group_media_players_content_verification"))
    testsuite.addTest(EnGroupMediaPlayersContentVerificationHelp("test_en_group_media_players_content_verification_help"))
    testsuite.addTest(EnGroupMediaPlayersFunctionDragAndDrop("test_en_group_media_players_function_drag_and_drop"))
    testsuite.addTest(EnGroupMediaPlayersFunctionModification("test_en_group_media_players_function_modification"))
    testsuite.addTest(EnGroupMediaPlayersFunctionSearch("test_en_group_media_players_function_search"))


    filename = gb_filename_prefix+'/GroupMediaPlayers.html'
    fp = file(filename,'wb')

    runner = HTMLTestRunner(
            stream=fp,
            title='groupMediaPlayer',
            description='Test Report'
            )
 #   runner = unittest.TextTestRunner()
    runner.run(testsuite)
