class ProductNew:
    ID = "NA"
    Quantity = 0
    Cost = 0

    def __init__(self, pdtID, qty, cost):
        self.ID = pdtID
        self.Quantity = qty
        self.Cost = cost 

    def print_Text(self):
        print(f"Details: {self.ID}-{self.Quantity}-{self.Cost}")

p1 = ProductNew("Laptop", 2, 50000)

class DemoConstructor:

    def __init__(self, *args):
        if len(args):
            pass
        if len(args) == 2:
            self.name, self.id = args
        elif len(args) == 3:
            self.name, self.id, self.subject = args

d1 = DemoConstructor()
d2 = DemoConstructor("lak", 111)
d3 = DemoConstructor("lak", 111, "python")
