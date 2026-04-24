# static attribute(class attribute)
# static method @staticmethod
# class method @classmethod

class Shopping:
    cart = [] # class attribute # static attribute
    origin = 'china'
    
    def __init__(self, name, location):
        self.name = name # instance attribute
        self.location = location
        
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')
        
    # static method
    @staticmethod
    def multiply(a, b):
        # print(self.name) # it is not possible inside the static method
        result = a*b
        print(result)
        
    @classmethod # decorator
    def hudai_dekhi(self, name, item):
        print(f'hey my name is {name}')
        print('hudai dekhi kintu kinmu na, just ac er haowa khaite aschi', item)
        
        
# Shopping.purchase('a', 's', 4, 6)

basundhara = Shopping('Bosundhara', 'Karwoan bazar')
# basundhara.purchase('lungi', 500, 1000)

basundhara.hudai_dekhi('munim', 'ami')
Shopping.hudai_dekhi('munim', 'ami')

# static method use in those time, when i want to use it without instance
Shopping.multiply(4, 6)
basundhara.multiply(6, 9)