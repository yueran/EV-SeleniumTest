#Tested functions: create manufacture, delete manufacture, modify the name of an existing manufacture.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *
#Office
#manTestValue = 40
#Home
#manTestValue = 6
class EnCreateProductsFunctionCreateManufacture(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_products_function_create_manufacture(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/createproducts")
        try: self.assertIn(createProductsManModifyText, driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(createProductsManModifySuccessText, driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("--New Manufacturer--")
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys("MCreateSuccess")
        driver.find_element_by_id("newManufacturer").click()
        driver.refresh()
        try: self.assertIn("MCreateSuccess", driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text(createProductsManModifyText)
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys(createProductsManModifySuccessText)
        driver.find_element_by_id("saveManufacturer").click()
        driver.refresh()
        for i in range(60):
            try:
                if "--New Manufacturer--" == driver.find_element_by_id("anyManufacturer").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
#        try: self.assertNotIn(createProductsManModifyText, driver.find_element_by_id("detailManufacturer").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(createProductsManModifySuccessText, driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
#        try: self.assertNotIn(createProductsManModifyText, driver.find_element_by_id("detailManufacturer").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn(createProductsManModifySuccessText, driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text(createProductsManModifySuccessText)
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("manufacturerName").clear()
        driver.find_element_by_id("manufacturerName").send_keys(createProductsManModifyText)
        driver.find_element_by_id("saveManufacturer").click()
        for i in range(60):
            try:
                if "--New Manufacturer--" == driver.find_element_by_id("anyManufacturer").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.refresh()
        try: self.assertIn(createProductsManModifyText, driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn(createProductsManModifySuccessText, driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("MCreateSuccess")
        driver.find_element_by_id("addManufacturer").click()
        driver.find_element_by_id("deleteManufacturer").click()
        driver.find_element_by_id("popup_ok").click()
        try: self.assertNotIn("MCreateSuccess", driver.find_element_by_id("detailManufacturer").text)
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
