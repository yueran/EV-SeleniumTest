# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import unicodedata
from Webdriver.all_globals import *


class LoginLanguageSelectionNl(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)

    def test_login_language_selection_nl(self):
        driver = self.driver
        driver.get(self.base_url + "/ev/login")
        Select(driver.find_element_by_css_selector("select.languageSelection")).select_by_visible_text("Nederlands")
        driver.implicitly_wait(30)
        for i in range(60):
            try:
                if u"Login Pagina" == driver.title: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(u"Login Pagina", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Welkom", driver.find_element_by_class_name("txtWelcome").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("form.password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"OK", driver.find_element_by_css_selector("span.commonButton.login_ok").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Je ID vergeten?", driver.find_element_by_id("txtForgotID").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Je wachtwoord vergeten?", driver.find_element_by_id("txtForgotPassword").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        gb_is_element_present(self, how, what)

    def tearDown(self):
        gb_tearDown(self)

if __name__ == "__main__":
    unittest.main()
