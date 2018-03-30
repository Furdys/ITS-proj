Feature: Checkout
	Background:
		Given an eshop selling iMac
		And user with iMac in shopping cart

	# STEP ONE MISSING

	Scenario: Not filling in required fields in billing details
		Given a web browser at checkout page step 2
		And <required> field is empty
		When user clicks on "Continue" button
		Then a warning below <required> field is shown
		
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
			
	Scenario: Filling in required fields in billing details
		Given a web browser at checkout page step 2
		And all required fields are filled in		
		When user clicks on "Continue" button
		Then step 4 is shown to the user
	
	Scenario: 
		Given a web browser at checkout page step 2
		And Checkbox "My delivery and billing addresses are the same." <boolean> checked
		When user clicks on "Continue" button
		Then step <number> is shown to the user
		
		Examples:
			| boolean | number |
			| is      | 4      |
			| isn't   | 3      |
			
	Scenario: Not filling in required fields in delivery details
		Given a web browser at checkout page step 2
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
			
	Scenario: Filling in required fields in delivery details
		Given a web browser at checkout page step 3
		And all required fields are filled in		
		When user clicks on "Continue" button
		Then step 4 is shown to the user
	

	Scenario: Not accepting Terms & Conditions
		Given a web browser at checkout page step 5
		And user doesn't check the "I have read and agree to the Terms & Conditions" box
		When user clicks on "Continue" button
		Then a warning is shown
		
	Scenario: Accepting Terms & Conditions
		Given a web browser at checkout page step 5
		And user check the "I have read and agree to the Terms & Conditions" box
		When user clicks on "Continue" button
		Then step 6 is shown to the user

	Scenario: Confirming order
		Given a web browser at checkout page step 6
		When user clicks on "Continue" button
		Then user is redirected to success page
