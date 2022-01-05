class Product(object):
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
p1 = Product('IPhone X',1200)
p2 = Product('Samsung',500)

print(p1.name,p1.price)
print(p2.name,p2.price)