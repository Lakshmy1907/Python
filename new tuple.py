# Inventory date as tuples(item_name,quantity,unit_price)
inventory = [("Laptop",12,40000.0),
             ("Keyboard",13,1200.0),
             ("Mouse",18,800.00),
             ("Headphone",5,150.00)]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name, quantity, unit_price=item
    stock_value=quantity*unit_price
    print(f"Item Name :{item_name},the total value is:{stock_value}")
    if stock_value> highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"Highest stock value is:{highest_stock_value}")
print(f"Item with highest stock value is:{item_with_highest_stock_value}")

