from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnUploadMediaFunctionModifyMedia(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_upload_media_function_modify_media(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/uploadmedia")
#        try: self.assertIn(uploadMediaOriginalMedia, driver.find_element_by_id("mediaBrowser").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(uploadMediaModifiedMedia, driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("media_medium"+TestMediaIdValue+"Options").click()
        driver.find_element_by_id("inputInfo").clear()
        driver.find_element_by_id("inputInfo").send_keys("MediaSuccess.avi")
        driver.find_element_by_id("okExistingMedia").click()
        for i in range(60):
            try:
                if u"MediaSuccess.avi" == driver.find_element_by_css_selector("#media_medium"+TestMediaIdValue +"> div.mediaBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertNotIn(u"MediaEditTest.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(u"MediaSuccess.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_id("media_medium"+TestMediaIdValue+"Options").click()
        driver.find_element_by_id("inputInfo").clear()
        driver.find_element_by_id("inputInfo").send_keys("MediaEditTest.avi")
        driver.find_element_by_id("okExistingMedia").click()
        for i in range(60):
            try:
                if u"MediaEditTest.avi" == driver.find_element_by_css_selector("#media_medium"+TestMediaIdValue +"> div.mediaBg.itemContent > div.blockText").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn(u"MediaEditTest.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(u"MediaSuccess.avi", driver.find_element_by_id("mediaBrowser").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
