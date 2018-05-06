Feature: Product listing


	Scenario: Display subcategories list
		Given a web browser is at e-shop homepage
		When user clicks on "Components" category
		Then dropmenu is shown containing following subcategories:
			| subcategory         |
			| Mice and Trackballs |
			| Monitors            |
			| Printers            |
			| Scanners            |
			| Web Cameras         |

	Scenario: Display empty subcategory
		Given a web browser is at e-shop homepage
		And "Components" category dropmenu is shown
		When user clicks on "Mice and Trackballs"
		Then user is displayed "There are no products to list in this category"
		
	Scenario: Display subcategory
		Given a web browser is at e-shop homepage
		And "Components" category dropmenu is shown
		When user clicks on "Monitors"
		Then user is displayed folowing products:
			| product                  |
			| Apple Cinema 30"         |
			| Samsung SyncMaster 941BW |
