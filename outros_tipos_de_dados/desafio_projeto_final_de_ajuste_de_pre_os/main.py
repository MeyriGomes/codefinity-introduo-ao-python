grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
price = grocery_inventory["Eggs"][1]
if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, old_price, qty = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, old_price - 1, qty)
else:
    print("The price of Eggs is reasonable.")
    
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)  
print("Inventory after adding Tomatoes:", grocery_inventory)

if "Milk" in grocery_inventory:
    if grocery_inventory["Milk"][2] < 10:
        print("Milk needs to be restocked. Increasing stock by 20 units.")
        cat, price, stock = grocery_inventory["Milk"]
        grocery_inventory["Milk"] = (cat, price, stock + 20)
    else:
        print("Milk has sufficient stock.")

if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price")

print("Updated inventory:",  grocery_inventory)


