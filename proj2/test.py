#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import time

class WebDriver(unittest.TestCase):
	def setUp(self):
		"""
		self.driver = webdriver.Remote(
			command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub",
			desired_capabilities=DesiredCapabilities.CHROME)
		"""
		dp = {'browserName': 'firefox', 'marionette': 'true',
			'javascriptEnabled': 'true'}
		self.driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
			desired_capabilities=dp)
		self.driver.implicitly_wait(15)
		self.base_url = "http://mys01.fit.vutbr.cz:8016"
		
		
	def addiMacToCart(self):
		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=product/product&path=20_27&product_id=41")
		self.driver.find_element_by_id("button-cart").click()			
		
	def test_addToCart(self):
		self.addiMacToCart()
		
		text = self.driver.find_element_by_css_selector("div.alert.alert-success").text
		
		self.assertEqual("Success: You have added iMac to your shopping cart!\n×", text)
		
	def test_checkItemsInCart(self):
		self.addiMacToCart()
		self.driver.get(self.base_url)
		
		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/cart")
		
		text = self.driver.find_element_by_css_selector("table.table.table-bordered > tbody > tr > td.text-left").text
		
		self.assertEqual("iMac", text)	

	
	def test_removeFromCart(self):
		self.addiMacToCart()
		
		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/cart")
		self.driver.find_element_by_css_selector("span.input-group-btn > button.btn.btn-danger").click()
	
		text = self.driver.find_element_by_css_selector("#content > p").text
	
		self.assertEqual("Your shopping cart is empty!", text)


	def test_changeItemQuantityInCart(self):
		self.addiMacToCart()
		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/cart")
		
		
		self.driver.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").clear()
		self.driver.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").send_keys("2")
		self.driver.find_element_by_css_selector("button.btn.btn-primary").click()
		
		text = self.driver.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").get_attribute("value")

		self.assertEqual("2", text)
		

	
	def test_displaySubcategoriesList(self):
		self.driver.get(self.base_url)
		self.driver.find_element_by_xpath("//a[contains(text(),'Components')]").click()

		self.assertEqual("Mice and Trackballs (0)", self.driver.find_element_by_xpath("//li[@class='dropdown open']//div//ul//li[1]//a").text)
		self.assertEqual("Monitors (2)", self.driver.find_element_by_xpath("//li[@class='dropdown open']//div//ul//li[2]//a").text)
		self.assertEqual("Printers (0)", self.driver.find_element_by_xpath("//li[@class='dropdown open']//div//ul//li[3]//a").text)
		self.assertEqual("Scanners (0)", self.driver.find_element_by_xpath("//li[@class='dropdown open']//div//ul//li[4]//a").text)
		self.assertEqual("Web Cameras (0)", self.driver.find_element_by_xpath("//li[@class='dropdown open']//div//ul//li[5]//a").text)
		
	def test_displayEmptySubcategory(self):
		self.driver.get(self.base_url)

		self.driver.find_element_by_xpath("//a[contains(text(),'Components')]").click()
		self.driver.find_element_by_css_selector("li.dropdown.open > div.dropdown-menu > div.dropdown-inner > ul.list-unstyled > li > a").click()
		
		text = self.driver.find_element_by_css_selector("#content > p").text
	
		self.assertEqual("There are no products to list in this category.", text)

	
	def test_displaySubcategory(self):
		self.driver.get(self.base_url)
		
		self.driver.find_element_by_xpath("//a[contains(text(),'Components')]").click()
		self.driver.find_element_by_xpath("//a[contains(text(),'Monitors (2)')]").click()
		
		self.assertEqual("Apple Cinema 30\"", self.driver.find_element_by_xpath("//a[contains(text(),'Apple Cinema 30\"')]").text)
		self.assertEqual("Samsung SyncMaster 941BW", self.driver.find_element_by_xpath("//a[contains(text(),'Samsung SyncMaster 941BW')]").text)

		
		
	"""
	def loginTestUser(self):
		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=account/login")
		#self.driver.find_element_by_id("input-email").clear()
		self.driver.find_element_by_id("input-email").send_keys("aaa@bbb.com")
		self.driver.find_element_by_id("input-password").send_keys("12345")
		self.driver.find_element_by_css_selector("input.btn.btn-primary").click()
	"""

	def test_startingCheckout(self):
		self.addiMacToCart()
		
		self.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[5]/a").click()
		
		time.sleep(1)
		
		self.assertEqual("panel-collapse collapse in", self.driver.find_element_by_id("collapse-checkout-option").get_attribute("class"))
	
		#self.loginTestUser()

		
if __name__ == "__main__":
	unittest.main()
