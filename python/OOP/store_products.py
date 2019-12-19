class Store:
    def __init__(self, name):
        self.name = name
        self.products = []


    def add_product(self,new_product):
        print("adding ",new_product)
        self.products.append(new_product)
        return self



class Product:
    def __init__(self, product_name="", price=0, category=""):
        self.product_name = product_name
        self.price = price
        self.category = category

    def update_price(self, percent_changed, is_increased):
        if is_increased == True:
            self.price = self.price+(self.price*percent_changed)
        elif is_increased == False:
            self.price = self.price-(self.price*percent_changed)
        return self

    def print_info(self):
        print(self.product_name,self.category,self.price)
        return self

store1 = Store("store1")
store2 = Store("store2")
banana = Product("banana",.11,"fruit")
milk = Product("milk",1.89,"dairy")

store1.add_product(Product(banana))
banana.print_info()
# product1.print_info()
# product1.update_price(.10,True).print_info()
# product2.print_info()
# product2.update_price(.2,False).print_info()

