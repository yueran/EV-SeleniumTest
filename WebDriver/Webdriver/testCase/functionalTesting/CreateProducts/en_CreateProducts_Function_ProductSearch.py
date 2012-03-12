from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
#Search product xpath;'//li[@id='products_category73']/div/span'
class EnCreateProductsFunctionProductSearch(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_products_function_product_search(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/createproducts")
        Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("Product")
        #driver.find_element_by_css_selector("div.blockText.selectedText").click()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        #home
        #driver.find_element_by_css_selector("#products_category73 > div.categoryBg.itemContent > span.fold").click()
        try: self.assertIn("abcd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("acccd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invuepro1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invuepro2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invueacc1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invueacc2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("ab")
        driver.find_element_by_id("productSearchButton").click()
        #driver.find_element_by_css_selector("div.blockText.selectedText").click()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        self.driver.implicitly_wait(100)
        for i in range(60):
            try:
                if u"abcd" == driver.find_element_by_xpath("//li[@id='products_product274']/div/div").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertIn("abcd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("acccd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invuepro1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invuepro2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invueacc1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invueacc2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("")
        Select(driver.find_element_by_id("selectedFilterValue")).select_by_visible_text("Invue Database")
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        self.driver.implicitly_wait(30)
        try: self.assertNotIn("abcd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("acccd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("invuepro1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("invuepro2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("invueacc1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("invueacc2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("productSearch").clear()
        driver.find_element_by_id("productSearch").send_keys("invuepro1")
        driver.find_element_by_id("productSearchButton").click()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        self.driver.implicitly_wait(30)
        try: self.assertNotIn("abcd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("acccd", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("invuepro1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invuepro2", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invueacc1", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertNotIn("invueacc2", driver.find_element_by_id("productSpace").text)
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
