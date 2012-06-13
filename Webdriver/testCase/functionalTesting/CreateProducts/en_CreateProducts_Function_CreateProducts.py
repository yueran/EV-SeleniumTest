#test function: create a product, modify its manufacture, category, Model, SKU, Price, description, addtional text, keywords.
#Note: drag and drop function is not added into this test case yet.
#Need to delete the product 'testMod' after testing.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver import ActionChains
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnCreateProductsFunctionCreateProducts(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_products_function_create_products(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/createproducts")
        driver.find_element_by_css_selector("div.bigDownArrow").click()
        #Office:
        #driver.find_element_by_css_selector("#products_category155 > div.categoryBg.itemContent > span.fold").click()
        #Home:
        #driver.find_element_by_css_selector("#products_category60 > div.categoryBg.itemContent > span.fold").click()
        try: self.assertNotIn("testMod", driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("newProduct").click()
        driver.find_element_by_id("product").click()
        try: self.assertIn("New Product", driver.find_element_by_id("productName").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        Select(driver.find_element_by_id("detailManufacturer")).select_by_visible_text("test")
#        Select(driver.find_element_by_id("detailCategory")).select_by_visible_text("ztest")
        driver.find_element_by_id("detailModel").clear()
        driver.find_element_by_id("detailModel").send_keys(createNewProduct)
        driver.find_element_by_id("detailSeries").clear()
        driver.find_element_by_id("detailSeries").send_keys("testSer")
        driver.find_element_by_id("detailPrice").clear()
        driver.find_element_by_id("detailPrice").send_keys("1000")
        driver.find_element_by_xpath("//div[@id='descriptionSection']/span").click()
        driver.find_element_by_css_selector("html").send_keys("test")
        driver.find_element_by_css_selector("span.mceIcon.mce_bold").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_italic").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_bold").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_italic").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_justifyleft").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_justifycenter").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_justifyright").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_justifyfull").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_bullist").click()
        driver.find_element_by_css_selector("span.mceIcon.mce_numlist").click()
        driver.find_element_by_xpath("//div[@id='additionalTextSection']/span").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "html"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        #driver.find_element_by_css_selector("html").clear()
        driver.find_element_by_css_selector("html").send_keys("test")
        driver.find_element_by_css_selector("#detailAdditionalText_bold > span.mceIcon.mce_bold").click()
        driver.find_element_by_css_selector("#detailAdditionalText_bold > span.mceIcon.mce_bold").click()
        driver.find_element_by_css_selector("#detailAdditionalText_italic > span.mceIcon.mce_italic").click()
        driver.find_element_by_css_selector("#detailAdditionalText_justifyleft > span.mceIcon.mce_justifyleft").click()
        driver.find_element_by_css_selector("#detailAdditionalText_justifycenter > span.mceIcon.mce_justifycenter").click()
        driver.find_element_by_css_selector("#detailAdditionalText_justifyright > span.mceIcon.mce_justifyright").click()
        driver.find_element_by_css_selector("#detailAdditionalText_justifyfull > span.mceIcon.mce_justifyfull").click()
        driver.find_element_by_css_selector("#detailAdditionalText_bullist > span.mceIcon.mce_bullist").click()
        driver.find_element_by_css_selector("#detailAdditionalText_numlist > span.mceIcon.mce_numlist").click()
        driver.find_element_by_xpath("//div[@id='keywordsSection']/span").click()
        #Select(driver.find_element_by_id("keywordSelect0")).select_by_visible_text("test")
        driver.find_element_by_id("saveProduct").click()
        try: self.assertTrue(self.is_element_present(By.ID, "previewProduct"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "deleteProduct"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.refresh()
        driver.find_element_by_css_selector("div.bigDownArrow").click()
##        driver.find_element_by_xpath("//li[@id='products_category"+classifyProductsNewCategoryIdValue+"\']/div/span").click()
        try: self.assertIn(createNewProduct, driver.find_element_by_id("productSpace").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_css_selector("div.bigDownArrow").click()
##        driver.find_element_by_xpath("//li[@id='products_category"+classifyProductsNewCategoryIdValue+"\']/div/span").click()
#        driver.find_element_by_xpath("//li[@id='products_category679']/div/span").click()
        createNewProductId = driver.find_element_by_xpath("//ul[@id='productBrowser']/li[5]").get_attribute("id")
        createNewProductIdValue = re.sub("\D","",createNewProductId)
        print "createNewProductIdValue=\""+ createNewProductIdValue+"\"\n"
        text_file = open(gb_Preprocess_ids_Prefix+"ids.py", "a")
        text_file.write("createNewProductIdValue=\""+ createNewProductIdValue+"\"\n")
        text_file.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
