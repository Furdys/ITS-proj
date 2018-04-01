Feature: Checkout
	Background:
		Given an eshop selling iMac
		And user with iMac in his shopping cart
	
	Scenario Outline: Starting checkout
		Given a web browser at e-shop homepage
		And user is <status>
		When user clicks on "Checkout" button
		Then step <number> is displayed to user
		
		Examples:
			| status        | number |
			| logged in     | 2      |
			| not logged in | 1      |
			
	Scenario: Checkout Options
		Given a web browser at checkout page step 1
		And user is not logged in
		When user clicks on "Continue"
		Then step 2 is displayed to user

	Scenario Outline: Account & Billing Details - Not filling in required fields
		Given a web browser at checkout page step 2
		And not logged in user chosed to register in checkout step 1
		And <required> field is empty
		When user clicks on "Continue" button
		Then a warning below <required> field is displayed
		
		Examples:
			| required         |
			| First Name       |
			| Last Name        |
			| E-Mail           |
			| Telephone        |
			| Password         |
			| Password Confirm |
			| Address 1        |
			| City             |
			| Post Code        |
			| Country          |
			| Region / State   |

	Scenario Outline: Billing Details - Not filling in required fields
		Given a web browser at checkout page step 2
		And "Guest Checkout" is selected in step 1
		And <required> field is empty
		When user clicks on "Continue" button
		Then a warning below <required> field is displayed
		
		Examples:
			| required       |
			| First Name     |
			| Last Name      |
			| E-Mail         |
			| Telephone      |
			| Address 1      |
			| City           |
			| Post Code      |
			| Country        |
			| Region / State |
	
	Scenario Outline: Billing Details - Filling in required fields in 
		Given a web browser at checkout page step 2
		And checkbox "My delivery and billing addresses are the same." is <state>
		And required fields are filled in
		When user clicks on "Continue" button
		Then step <number> is displayed to user
		
		Examples:
			| state       | number |
			| checked     | 4      |
			| not checked | 3      |
			
	Scenario: Delivery Details - Not filling in required fields
		Given a web browser at checkout page step 3
		And <required> field is empty
		When user clicks on "Continue" button
		Then a warning below <required> field is shown
	
		Examples:
			| required       |
			| First Name     |
			| Last Name      |
			| Address 1      |
			| City           |
			| Post Code      |
			| Country        |
			| Region / State |		
			
	Scenario: Delivery Details - Filling in required fields
		Given a web browser at checkout page step 3
		And all required fields are filled in		
		When user clicks on "Continue" button
		Then step 4 is displayed to user
		
	Scenario: Delivery Method
		Given a web browser at checkout page step 4
		When user clicks on "Continue" button
		Then step 5 is displayed to user		

	Scenario: Payment Method - Not accepting Terms & Conditions
		Given a web browser at checkout page step 5
		And user doesn't check the "I have read and agree to the Terms & Conditions" box
		When user clicks on "Continue" button
		Then a warning is displayed to user
		
	Scenario: Payment Method - Accepting Terms & Conditions
		Given a web browser at checkout page step 5
		And user check the "I have read and agree to the Terms & Conditions" box
		When user clicks on "Continue" button
		Then step 6 is displayed to user

	Scenario: Confirm Order
		Given a web browser at checkout page step 6
		When user clicks on "Confirm Order" button
		Then user is displayed "Your order has been placed!"
