Project Title: Cafe Restaurant
Overview of the project: This is a foundational command-line interface (CLI) application designed to simulate a basic item ordering and billing process for a small restaurant. The system allows users to interactively view a fixed menu, place an order for up to two items, and receive a calculated total bill.
Features: Fixed Menu Definition: Stores item names and corresponding prices using a robust dictionary structure.

Customer Greeting and Menu Display: Presents a welcoming message and a clear, readable list of all available menu items and their costs.

Item Validation: Checks if the requested item exists on the defined menu before processing the order.

Order Accumulation: Maintains a running Order_total by adding the price of each valid item ordered.

Sequential Ordering: Supports the ordering of up to two items, allowing the user to decide whether to add a second item after the first.

Final Billing: Outputs the calculated total amount due to the customer.

Technology: Language: Python 3 (Pure Python)

Environment: Command-Line Interface (CLI)

Steps to run the project: Save the Code:

Copy the Python code (the original ordering script) and save it in a file named restaurant_order.py (or any name ending with .py).

Open the Command Line:

Open your computer's terminal (Linux/macOS) or Command Prompt/PowerShell (Windows).

Navigate to the File:

Use the cd (Change Directory) command to move to the folder where you saved the restaurant_order.py file.

Example: If you saved it in a folder called Projects on your desktop, you would type:

Bash

cd Desktop/Projects
Execute the Script:

Run the script using the Python interpreter.

Type the following command and press Enter:

Bash

python restaurant_order.py
Note: On some systems, you might need to use python3 instead of python.

Follow the Prompts:

The program will start by greeting you and displaying the menu.

It will then prompt you for input. Type the name of the item you want to order (e.g., Pasta) and press Enter. Remember the item names are case-sensitive!

Instructions for testing: Step 1: Verify that a single valid item is added correctly to the total.
Step 2: Verify if you want to add another item.
Step 3: Verify that two valid items are added correctly to the total.
Step 4: Verify that the system handles a mixed order, rejecting the invalid item but accepting the valid one.
Step 5: Verify that the total comes out. 
Continue following the prompts for the second item (enter Yes or No).

The program will finally print the total amount due before exiting.
