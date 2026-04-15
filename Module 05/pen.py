# constructor
class Pen:
    def __init__(self, owner, brand, color, price):
        self.owner = owner
        self.brand = brand
        self.color = color
        self.price = price
        
    
my_pen = Pen('munim', 'matador', 'black', '5 taka')
print(my_pen.owner, my_pen.brand, my_pen.color, my_pen.price)


friend_pen = Pen('imran', 'ekono', 'blue', '7 taka')
print(friend_pen.owner, friend_pen.brand, friend_pen.color, friend_pen.price)

her_pen = Pen('Akash', 'fresh', 'red', '10 taka')
print(her_pen.owner, her_pen.brand, her_pen.color, her_pen.price)