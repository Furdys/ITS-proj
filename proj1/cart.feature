Feature: Shopping cart		

	Background:
		Given an eshop selling iMac

	Scenario: Add to cart
		Given a web browser is at iMac detail page
		When user clicks on "Add to Cart" button
		Then iMac is added to user's shopping cart
		
	Scenario: Check items in cart
		Given a web browser is at e-shop homepage
		And shopping cart contains iMac
		When user clicks on "Shopping Cart"
		Then the product and its price is shown
		
	Scenario: Remove item from cart
		Given a web browser is at shopping cart page
		And the shopping cart contains iMac		
		When user clicks on "Remove" button in iMac field
		Then iMac is removed from the shopping cart
					
	Scenario: Change item quantity in cart
		Given a web browser is at shopping cart page
		And the shopping cart contains one iMac
		When user write "2" in the iMac quantity field and clicks "Update" button
		Then the cart contains two iMacs	
