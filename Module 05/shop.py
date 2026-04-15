class Shop:
    cart = []  # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer
        
    def add_to_cart(self, item):
        self.cart.append(item)
        
munim = Shop('MMunim')
munim.add_to_cart('watch')
munim.add_to_cart('phone')
print(munim.cart)

nibir = Shop('nibir')
nibir.add_to_cart('cap')
nibir.add_to_cart('watch')
print(nibir.cart)