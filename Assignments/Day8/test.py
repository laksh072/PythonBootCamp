class Product:
   
    country = "no country defined"
    discount = 0   
       
    def __init__(self,*args):
        if len(args) == 0:
            self.product_id = None
            self.name = None
            self.price = None
            
        elif len(args) == 2:
            self.product_id, self.name = args
            self.price = 0
        elif len(args) == 4:
            self.product_id, self.name,self.price,self.country = args

    def setSelfCountry(self,name):
        self.country = name

 
pdt1 = Product()
print(f"Pdt1 - {pdt1.country}")
pdt1.country = "Static country"

# pdt2 = Product(101, 'Laptop', 80000, 'India')
pdt2 = Product(101, 'Laptop', 80000)
pdt2.setSelfCountry("india")
print(f"Pdt2 - {pdt2.country}")
print(f"Pdt1 - {pdt1.country}")
print(f"Pdt2 - {pdt2.country}")