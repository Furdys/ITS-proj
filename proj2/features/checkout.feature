Feature: Checkout

	Background:
		Given shopping cart contains iMac


	Scenario: Starting checkout
		Given a web browser is at e-shop homepage
		When user clicks on "Checkout" button
		Then step 1 is displayed to user

	Scenario Outline: Billing Details - Not filling in required fields
		Given a web browser at checkout page
		And "Guest Checkout" was selected in step 1
		And <required> field is empty
		When user clicks on "Continue" button
		Then a warning below <required> field is displayed

		Examples:
			| required       |
			| First Name     |
			| Last Name      |

	Scenario Outline: Billing Details - Filling in required fields in 
		Given a web browser at checkout page
		And "Guest Checkout" was selected in step 1
		And required fields are filled in
		When user clicks on "Continue" button
		Then step 3 is displayed to user
