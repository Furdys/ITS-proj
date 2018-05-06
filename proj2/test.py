#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class WebDriverChrome(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Remote(
			command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub",
			desired_capabilities=DesiredCapabilities.CHROME)
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
		
		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/cart")
		
		text = self.driver.find_element_by_css_selector("table.table.table-bordered > tbody > tr > td.text-left").text
		
		self.assertEqual("iMac", text)	
		
#	def test_removeFromCart(self):
#		self.addiMacToCart()
		
#		self.driver.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/cart")
#		self.driver.find_element_by_css_selector("span.input-group-btn > button.btn.btn-danger").click()
	
#		text = self.driver.find_element_by_css_selector("table.table.table-bordered > tbody > tr > td.text-left").text
		
#		self.assertEqual("iMac", text)	
	
		#text = self.driver.find_element_by_css_selector("#content > p").text
	
		#self.assertEqual("Your shopping cart is empty!", text)

		
if __name__ == "__main__":
	unittest.main()
