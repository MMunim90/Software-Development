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
        
sakib = Cricketer('sakib', 38, 68, 91, 'BD', 'All-rounder')
sakib.eat()
sakib.exercise()