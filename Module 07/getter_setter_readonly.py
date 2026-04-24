# read only ---> you can not set the value. value can not be changed.
# getter ---> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter ---> set a value of a property through a method. Most of the time, you will set the value of a private attribute.

class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money
        
    @property # convert method into attribute. This is a getter and getter without any setter is readonly attribute
    def age(self):
        return self._age
    
    @property # convert method into attribute. This is a getter and getter without any setter is readonly attribute
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value <= 0:
            return 'salary can not be zero or negative value'
        self.__money += value
        
samsu = User('Kopa', 21, 12000)
# print(samsu.__money)
# print(samsu.age())
print(samsu.age)
# print(samsu.salary())
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)