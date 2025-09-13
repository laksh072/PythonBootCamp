
# Scenario:
 
# You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
# Q1. Product Search System (Static Polymorphism)
# Problem Statement:
# Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
# Requirements:
# Use default arguments and/or *args, **kwargs to simulate method overloading.
# Allow the following types of searches:
# only by name
# Name and category
# Name, category, and price range
 
# Q2. Cart System with Quantity Variations (Static Polymorphism)
 
# Problem Statement:
# Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
# Requirements:
# Add multiple products at once with name and quantity
# Simulate static polymorphism using variable arguments
 
# Q3. Discount Application (Static Polymorphism)
 
# Problem Statement:
# Create a class Discount that allows applying different types of discounts:
# Flat discount
# Percentage discount
# Buy One Get One
# Use static polymorphism to overload the method using default parameters or *args
 

# Q4. Payment System (Dynamic Polymorphism)
 
# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
# Requirements:
# Override pay() method in each class to simulate different payment methods
 

# Q1. Product Search System (Static Polymorphism)

productlist = [
{
        "Name" : "Laptop",
        "Category" : "Electronic",
        "Price" : 50000
},
{
        "Name" : "Car",
        "Category" : "Vehicle",
        "Price" : 300000
},
{
        "Name" : "TV",
        "Category" : "Home",
        "Price" : 100000
},
]

class ProductSearch:

    def search(self, name = None, category = None, price = None):
        searchBy = "None"
        if name is not None and category is not None and price is not None:
            searchBy = "All"
        elif name is not None and category is not None:
            searchBy = "Name_Category"   
        elif name is not None:
            searchBy = "Name"

        product_found = None
        for product in productlist:
            match searchBy:
                case "All":
                    if (product["Name"] == name and product["Category"] == category and product["Price"] == price):
                        product_found = product
                        break
                case "Name_Category":
                    if (product["Name"] == name and product["Category"] == category):
                        product_found = product
                        break
                case "Name":
                    if (product["Name"] == name):
                        product_found = product
                        break
                case _ : pass
        if product_found is not None:
            print(f"Product : {product_found['Name']} Category : {product_found['Category']} Price : {product_found['Price']}")
        else:
            print(f"Product Not found")

psearch =  ProductSearch()
psearch.search("TV")
psearch.search("Car",  "Vehicle")
psearch.search("Laptop",  "Electronic", 50000)
psearch.search("NoItem")


class Cart:
    cartlist = []
    def addcart(self, *products):
        for item in products:
            self.cartlist.append({"Name" : item[0], "Quantity" : item[1]})
    def __repr__(self):
        return f"Cart list \n{self.cartlist}"

cart = Cart()
cart.addcart(("Laptop", 40), ("Table", 10))
cart.addcart(("Bicycle", 20))
print(cart)

class Discount:
    def ApplyDiscount(self, *dicountTypes):
        if len(dicountTypes) == 2:
            if dicountTypes[0] is not None and dicountTypes[1] is not None:
                if str(dicountTypes[0]).__contains__("Percentage"):
                    print(f"Discount By : {dicountTypes[0]} Percentage : {dicountTypes[1]}%")
                else:
                    print(f"Discount By : {dicountTypes[0]} Amount : Rs {dicountTypes[1]}")
        elif len(dicountTypes) == 1:
                print(f"Discount By : {dicountTypes[0]}")
        else:
            print("No discount")

dicount = Discount()
dicount.ApplyDiscount("Flat" , 200)
dicount.ApplyDiscount("Percentage" , 20)
dicount.ApplyDiscount("B1G1")
dicount.ApplyDiscount()


class Payment:
    def pay(self):
        print("Base class payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("Credit Card Payment")

class UPIPayment(Payment):
    def pay(self):
        print("UPI Payment")

class CODPayment(Payment):
    def pay(self):
        print("COD Payment")

payment = Payment()
payment.pay()
payment = CreditCardPayment()
payment.pay()
payment = UPIPayment()
payment.pay()
payment = CODPayment()
payment.pay()