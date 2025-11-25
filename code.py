#Define the menu of restaurant
menu = {
    'Pizza':100,
    'Pasta':80,
    'Burger':50,
    'Coffee':70,
    'Fries':60,
}

#Greet
print("Welcome to VITB Restaurant")
print("Pizza: Rs100\nPasta: Rs80\nBurger: Rs50\nCoffee: Rs70\nFries: Rs60\n")

Order_total = 0
#60 + 70 = 130

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    Order_total += menu[item_1] #0 + 80 
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        Order_total += menu[item_2] 
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {Order_total}")
