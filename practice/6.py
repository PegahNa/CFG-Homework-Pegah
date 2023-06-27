# You are trying to get rid of your old stuff in a bootsale and want to setup a program
# to quickly return the price when given an item.
# ●Create a ‘shop’ dictionary with at least 4 items and respective prices.
# ●Write some code that will take in the name of an item and output the price

shop = {
"Item1" : 10.99,
"Item2" : 7.50,
"Item3" : 5.25,
"Item4" : 12.00,
}

item_name = input("Enter the name of an item: ")
item_name = item_name.capitalize()
if item_name in shop:
    price = shop[item_name]
    print(f"The price of {item_name} is £{price: .2f}")
else:
    print("Item not found in the shop")