class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
        
    def show_cart_item(self):
        for i, item in enumerate(self.cart):
            print(f'item number: {i}, item: {item['item']}, price: {item['price']}, quantity: {item['quantity']}')
    
    def remove_item(self):
        self.show_cart_item()
        item = int(input('Type item number you want to remove: '))
        if self.cart.__len__() <= item:
            print('This item is not available in the list')
        else:
            print(f'If you want to remove {self.cart[item]['item']} item from the cart, type \'confirm\'')
            conf = input()
            if conf == 'confirm':
                print(f'{self.cart[item]['item']} is removed from the cart')
                del self.cart[item]
                print('Remaining cart item: ')
                self.show_cart_item()
            else:
                print('Character mismatch, try again!')
        
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
# munim.checkout(1000)
munim.remove_item()
# munim.show_cart_item()