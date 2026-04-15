class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
        
    def add_to_cart(self, item):
        self.cart.append(item)
        
munim = Shop('munim')
munim.add_to_cart('phone')
munim.add_to_cart('watch')
print(munim.cart)

nibir = Shop('nibir')
nibir.add_to_cart('cap')
nibir.add_to_cart('shirt')
print(nibir.cart)

imran = Shop('imran')
imran.add_to_cart('pant')
imran.add_to_cart('sunglass')
print(imran.cart)