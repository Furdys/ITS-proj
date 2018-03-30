Feature: Shopping cart

	Background:
		Given an eshop containing products:
			| product                  |
			| iMac                     |
			| Apple Cinema 30"         |
			| Samsung SyncMaster 941BW |
			| Samsung Galaxy Tab 10.1  |
			| HTC Touch HD             |
			| iPhone                   |
			| Palm Treo Pro            |
			| Canon EOS 5D             |
			| Nikon D300               |			

	Scenario Outline: Add to cart
		Given a web browser is at <product> detail page
		When user clicks on "Add to Cart" button
		Then <product> is added to user's shopping cart
		
	Scenario Outline: Check items in cart
		Given a web browser is at e-shop homepage
		And shopping cart contains <product>
		When user clicks on "Shopping Cart"
		Then <product> and its price is shown
		
	Scenario Outline: Remove item from cart
		Given a web browser is at shopping cart page
		And the shopping cart contains <product>		
		When user click "Remove" button
		Then <product> is removed from the shopping cart
					
	Scenario Outline: Change item quantity in cart
		Given a web browser is at shopping cart page
		And the shopping cart contains one <product>
		When user write "2" in <product> quantity field and clicks "Update" button
		Then the cart contains <product> twice	
