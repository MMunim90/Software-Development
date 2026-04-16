class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
    
    def remove_item(self, item):
        pass
        
    def total_price(self):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        # print('Total price you have to pay: ', total)
        return total
        
    def checkout(self, amount):
        if amount < self.total_price():
            print(f'Please provide {self.total_price() - amount} taka more')
        else:
            if amount > self.total_price():
                extra = amount - self.total_price()
                print(f'Thank you for your purchase. Please receive your items and extra money: {extra}')
            else:
                print(f'Thank you for your purchase.  Please receive your items')
        
munim = Shopping('munim')
munim.add_to_cart('alu', 50, 6)
munim.add_to_cart('dim', 12, 24)
munim.add_to_cart('rice', 50, 5)

# print(munim.cart)

# munim.total_price()
munim.checkout(1000)
