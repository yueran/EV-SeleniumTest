from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from Webdriver.all_globals import *
from Webdriver.contentMaintenance import *
from Webdriver.testPreProcess.ids import *
from Webdriver.testPreProcess.input import *

class EnCreateProductsContentVerification(unittest.TestCase):
    def setUp(self):
        gb_setUp(self)
    
    def test_en_create_products_content_verification(self):
        driver = self.driver
        gb_login(self)
        driver.get(self.base_url + "/ev/createproducts")
        gb_frame(self)
        driver.find_element_by_id("productSearchButton").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.corporateLogo"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Products", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Create Products", driver.find_element_by_id("pageTitle").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header']/div[2]/div[2]/a/button"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.columnHeaderText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Search Products", driver.find_element_by_css_selector("span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Product", driver.find_element_by_id("selectedFilterValue").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Invue Database", driver.find_element_by_id("selectedFilterValue").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "productSearch"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_id("productSearchButton").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Please Select a Product", driver.find_element_by_id("selectProduct").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.blockText.selectedText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("div.bigDownArrow").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Save", driver.find_element_by_css_selector("#productDetailSpace > div.columnHeader > div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Preview", driver.find_element_by_css_selector("#productDetailSpace > div.columnHeader > div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Delete", driver.find_element_by_css_selector("#productDetailSpace > div.columnHeader > div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("New", driver.find_element_by_css_selector("#productDetailSpace > div.columnHeader > div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "saveProduct"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "newProduct"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Setup Product or Accessory", driver.find_element_by_id("productName").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "label"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='productDetailSpace']/div/div[2]/label[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertEqual("Manufacturer:", driver.find_element_by_xpath("//div[@id='productDetailSpace']/div/div[3]/div/span[2]").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Manufacturer:", driver.find_element_by_class_name("productBoxes").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("--New Manufacturer--", driver.find_element_by_id("detailManufacturer").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "addManufacturer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertEqual("Category:", driver.find_element_by_xpath("//div[@id='productDetailSpace']/div/div[3]/div[2]/span").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Category:", driver.find_element_by_class_name("productBoxes").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "detailCategory"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Model:", driver.find_element_by_class_name("productBoxes").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("SKU:", driver.find_element_by_class_name("productBoxes").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertIn("Price:", driver.find_element_by_class_name("productBoxes").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "detailModel"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "detailSeries"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "detailPrice"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Product Image 1 (slide show)", driver.find_element_by_css_selector("#slideshowSection > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertEqual("+ AddImage", driver.find_element_by_css_selector("h2.mediaHeader").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertEqual("Drag and DropImage\nfrom the Media list\n4:3\n720 px x 538 px\n(or higher for best results)", driver.find_element_by_css_selector("div.mediaBackground.uploadImage").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Product Image 2", driver.find_element_by_css_selector("#secondaryImageSection > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertEqual("+ AddImage", driver.find_element_by_css_selector("#staticImageAssign > h2.mediaHeader").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Video", driver.find_element_by_css_selector("#videoSection > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertEqual("Drag and DropVideo\nfrom the Media list\n16:9\n1280 px x 720 px\n(or higher for best results)", driver.find_element_by_css_selector("div.mediaBackground.uploadVideo > span.spanText").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Product Description", driver.find_element_by_css_selector("#descriptionSection > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#videoSection > span.fold.unfolded"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#descriptionSection > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_bold").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_italic").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_justifyleft").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_justifycenter").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_justifyright").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_justifyfull").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_bullist").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.mceIcon.mce_numlist").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#additionalTextSection > div.blockText"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#additionalTextSection > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_bold > span.mceIcon.mce_bold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_italic > span.mceIcon.mce_italic"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_justifyleft > span.mceIcon.mce_justifyleft"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_justifycenter > span.mceIcon.mce_justifycenter"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_justifyright > span.mceIcon.mce_justifyright"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_justifyfull > span.mceIcon.mce_justifyfull"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_bullist > span.mceIcon.mce_bullist"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#detailAdditionalText_numlist > span.mceIcon.mce_numlist"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Keywords", driver.find_element_by_css_selector("#keywordsSection > div.blockText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#keywordsSection > span.fold"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#mediaSpace > div.columnHeader"))
        try: self.assertEqual("Media", driver.find_element_by_css_selector("#mediaSpace > div.columnHeader > span.columnHeaderText").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(self.is_element_present(By.ID, "mediaSearchText"))
        try: self.assertTrue(self.is_element_present(By.ID, "mediaSearchButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.uploadNewMedia.commonButton"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertEqual("", driver.find_element_by_css_selector("span.uploadMediaButton.adder").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.ID, "footer"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.footerLogoImg > img"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='footer']/div").text)
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
