# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
# Access and print the second element of the tuple product.
# Slice and print the last two elements of the product tuple.
# Check whether "Electronics" is present in the product tuple and print a message. 
# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
# Find and print the maximum and minimum price from the prices tuple.
# Use a loop to print each item from the product tuple on a new line.
# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
# Unpack the tuple product into three variables and print each variable.
# Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.

product_tuple = ("Laptop", 50000, "Black", 'Samsung', "Electronics")
print("Tuple details:", product_tuple)
print("Second element :", product_tuple[1])
print("Last two elements :", product_tuple[-2:])

if "Electronics" in product_tuple:
    print("Electronics present")

prices = (1000, 1500, 1200, 1100, 900)
print("Count of 1000:", prices.count(1000)) 
print("Maximum price :", max(prices))
print("Minimum price is:", min(prices))

for item in product_tuple:
    print(item)

product_list = list(product_tuple)
product_list[1] = 55000 # Change price

product_tuple = tuple(product_list)

product_tuple += ("In Stock",) # Adding new item

product_list = list(product_tuple) # Note: convert to list for any add or remove operation
product_list.remove("Electronics") # Removing item
product_tuple = tuple(product_list)
print("Updated tuple :", product_tuple)

# Unpacking
name, price, color, brand, availability = product_tuple
print("Name:", name)
print("Price:", price)
print("Color:", color)
print("Brand:", brand)
print("Availability:", availability)

nested_pdt_tuple = (("Laptop", 50000, "Black", 'Samsung', "Electronics"), 
                   ("Phone", 150000, "White", 'Apple', "Electronics"), 
                   ("Tablet", 20000, "Blue", 'Lenovo', "Electronics"))
print("2nd product details:", nested_pdt_tuple[1][0], nested_pdt_tuple[1][1], nested_pdt_tuple[1][2], nested_pdt_tuple[1][3], nested_pdt_tuple[1][4])
