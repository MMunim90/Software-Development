# overload plus sign

# print(45 + 63)
# print('sakib' + 'al' + 'hasan')
# print([12, 98] + [5, 6, 7, 1, 2])

# adding two class

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def eat(self):
        print('vat, mangso, polau, korma')
        
    def exercise(self):
        raise NotImplementedError
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team, role):
        self.team = team
        self.role = role
        super().__init__(name, age, height, weight)
        
    # override
    def eat(self):
        print('vegetables, fruits, honey-nuts')
        
    def exercise(self):
        print('doing gym properly to better perform in match')
        
    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len operator overload
    def __len__(self):
        return self.height
    
    # > sign operator overload
    def __gt__(self, other):
        return self.age > other.age
    
sakib = Cricketer('sakib', 38, 68, 91, 'BD', 'All-rounder')
mushi = Cricketer('mushi', 36, 65, 78, 'BD', 'Batter, Wicket Keeper')

print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)