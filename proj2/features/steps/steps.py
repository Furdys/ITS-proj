#!/usr/bin/env python3

@given("a web browser is at iMac detail page")  
def step(context):
	context.browser.get("http://mys01.fit.vutbr.cz:8016/index.php?route=product/product&path=20_27&product_id=41")

@when('user clicks on "Add to Cart" button')
def step(context):
	context.browser.find_element_by_id("button-cart").click()
	
@then("iMac is added to user's shopping cart")
def step(context):
	text = context.browser.find_element_by_css_selector("div.alert.alert-success").text[:-2]
	assert(u"Success: You have added iMac to your shopping cart!" == text)
"""		
		
@given("a web browser is at e-shop homepage")  
def step(context):
	context.browser.get(context.base_url)		
		
@given("shopping cart contains iMac")  	
def step(context):
	context.browser.get("http://mys01.fit.vutbr.cz:8016/index.php?route=product/product&path=20_27&product_id=41")
	context.browser.find_element_by_id("button-cart").click()	

@when('user clicks on "Shopping Cart"')
def step(context):
	context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[4]/a/span").click()
	
@then("iMac is displayed to user")
def step(context):
	text = context.browser.find_element_by_css_selector("table.table.table-bordered > tbody > tr > td.text-left").text
	assert(u"iMac" == text)
"""
