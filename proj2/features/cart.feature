Feature: Shopping cart		

	Scenario: Add to cart
		Given a web browser is at iMac detail page
		When user clicks on "Add to Cart" button
		Then iMac is added to user's shopping cart

	Scenario: Check items in cart
		Given a web browser is at e-shop homepage
		And shopping cart contains iMac
		When user clicks on "Shopping Cart"
		Then iMac is displayed to user
