Problem Statement: The challenge is to create a minimal, functional prototype for a restaurant's ordering system using a command-line 
interface (CLI). The system must be able to accurately store and validate orders against a fixed menu, calculate the running total, 
and guide the user through a sequential ordering process of up to two items. This serves as a foundational exercise in applying Python's 
core structures (dictionaries, variables, and conditional logic) to solve a simple, real-world transaction management problem.

Scope of the project: the scope is to demonstrate the use of fundamental programming constructs (dictionary, if/else, and input/print) to
execute a single, two-step transactional loop, running entirely within a terminal environment. It deliberately avoids advanced features like 
loops for unlimited ordering, quantity selection, or persistent data storage.

Target Users: The End-User (Customer) and The Educational/Demonstration User (Fresher Student/Developer)

High level features: Fixed Menu Definition: Stores the available items and their prices using a Python dictionary.

Customer Greeting and Menu Display: Presents the user with a welcome message and a clear list of all items and costs.

Item Validation: Checks the existence of requested items on the menu before adding them to the order.

Order Accumulation: Maintains a running total (Order_total) of the cost for all valid items.

Sequential Ordering: Manages the order flow, allowing the user to select up to two items.

Final Billing: Outputs the calculated total amount due to the customer upon completion of the ordering process.
