#!/usr/bin/env python3

import time


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



@given("a web browser is at e-shop homepage")  
def step(context):
	context.browser.get(context.base_url)		
		
@given("shopping cart contains iMac")  	
def step(context):
	prevUrl = context.browser.current_url
	context.browser.get("http://mys01.fit.vutbr.cz:8016/index.php?route=product/product&path=20_27&product_id=41")
	context.browser.find_element_by_id("button-cart").click()	
	context.browser.get(prevUrl)

@when('user clicks on "Shopping Cart"')
def step(context):
	context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[4]/a/span").click()
	
@then("iMac is displayed to user")
def step(context):
	text = context.browser.find_element_by_css_selector("table.table.table-bordered > tbody > tr > td.text-left").text
	assert(u"iMac" == text)



@given("a web browser is at shopping cart page")  
def step(context):
	context.browser.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/cart")	
	
@when('user clicks on "Remove" button in iMac field')
def step(context):
	context.browser.find_element_by_css_selector("span.input-group-btn > button.btn.btn-danger").click()
	
@then("iMac is removed from the shopping cart")
def step(context):
	text = context.browser.find_element_by_css_selector("#content > p").text
	assert(u"Your shopping cart is empty!" == text)
	
	
@when('user write "2" in the iMac quantity field and clicks "Update" button')
def step(context):
	context.browser.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").clear()
	context.browser.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").send_keys("2")
	context.browser.find_element_by_css_selector("button.btn.btn-primary").click()
	
@then("shopping cart contains two iMacs")
def step(context):
	text = context.browser.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").get_attribute("value")
	assert(u"2" == text)
	
	
@when('user clicks on "Components" category')
def step(context):
	context.browser.find_element_by_xpath("//a[contains(text(),'Components')]").click()
	
@then("dropmenu is shown containing following subcategories")
def step(context):
	i = 1
	for row in context.table:	
		assert(row["subcategory"] == context.browser.find_element_by_xpath("//li[@class='dropdown open']//div//ul//li["+str(i)+"]//a").text[:-4])
		i = i+1
		
		
@given('"Components" category dropmenu is shown')
def step(context):
	context.browser.find_element_by_xpath("//a[contains(text(),'Components')]").click()	
	
@when('user clicks on "Mice and Trackballs"')
def step(context):
	context.browser.find_element_by_css_selector("li.dropdown.open > div.dropdown-menu > div.dropdown-inner > ul.list-unstyled > li > a").click()
	
@then('user is displayed "There are no products to list in this category"')
def step(context):
	text = context.browser.find_element_by_css_selector("#content > p").text
	assert(u"There are no products to list in this category." == text)	
	
@when('user clicks on "Monitors"')
def step(context):
	context.browser.find_element_by_xpath("//a[contains(text(),'Monitors (2)')]").click()

@then("user is displayed folowing products")
def step(context):
	for row in context.table:
		assert(row["product"] == context.browser.find_element_by_xpath("//a[contains(text(),'"+row["product"]+"')]").text)
	
	
@when('user clicks on "Checkout" button')
def step(context):
	context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[5]/a").click()
	
@then("step 1 is displayed to user")
def step(context):
	time.sleep(1)	
	assert(u"panel-collapse collapse in" == context.browser.find_element_by_id("collapse-checkout-option").get_attribute("class"))
	

@given("a web browser at checkout page")
def step(context):
	context.browser.get("http://mys01.fit.vutbr.cz:8016/index.php?route=checkout/checkout")
	
@given('"Guest Checkout" was selected in step 1')
def step(context):
	context.browser.find_element_by_xpath("(//input[@name='account'])[2]").click()
	context.browser.find_element_by_id("button-account").click()
	
@given("First name field is empty")
def step(context):
	context.browser.find_element_by_id("input-payment-firstname").clear()
	
@given("Last name field is empty")
def step(context):
	context.browser.find_element_by_id("input-payment-lastname").clear()
	
@when('user clicks on "Continue" button')
def step(context):
	context.browser.find_element_by_id("button-guest").click()

@then("a warning below First name field is displayed")
def step(context):
	
	text = context.browser.find_element_by_xpath("//div[starts-with(text(), 'First Name must')]").text
	assert(u"First Name must be between 1 and 32 characters!" == text)
	
@then("a warning below Last name field is displayed")
def step(context):
	text = context.browser.find_element_by_xpath("//div[starts-with(text(), 'Last Name must')]").text
	assert(u"Last Name must be between 1 and 32 characters!" == text)
	
	
@given("required fields are filled in")
def step(context):
	context.browser.find_element_by_id("input-payment-firstname").send_keys("aaa")
	context.browser.find_element_by_id("input-payment-lastname").send_keys("bbb")
	context.browser.find_element_by_id("input-payment-email").send_keys("aaa@bbb.com")
	context.browser.find_element_by_id("input-payment-telephone").send_keys("123456789")
	context.browser.find_element_by_id("input-payment-address-1").send_keys("ccc")
	context.browser.find_element_by_id("input-payment-city").send_keys("ddd")
	context.browser.find_element_by_id("input-payment-postcode").send_keys("12345")
	context.browser.find_element_by_xpath("(//option[@value='3513'])").click()
	
@then("step 3 is displayed to user")
def step(context):
	assert(u"panel-collapse collapse in" == context.browser.find_element_by_id("collapse-payment-method").get_attribute("class"))
	
