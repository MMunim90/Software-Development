class Product:
    def __init__(self, name):
        self.name = name

class Shop:
    def __init__(self):
        self.products_list = {}
    
    def add_product(self, item):
        self.products_list[item.name] = item
    
    def buy_product(self, item):
        if item in self.products_list:
            print(f'Congress!!! you successfully bought {item}')
            print(f'Here is your {item}')
        else:
            print(f'Sorry! This {item} is not in the product list')


shop = Shop()
p1 = Product('car')
p2 = Product('watch')

shop.add_product(p1)
shop.add_product(p2)

shop.buy_product('car')