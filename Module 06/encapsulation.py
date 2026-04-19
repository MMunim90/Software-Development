# encapsulation ---> hide details
# access modifier: public, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name # public attribute
        self._branch = 'banani 11' # protected attribute
        self.__balance = initial_deposit # private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'Not Enough Money'
        
rafsun = Bank('choooto bro', 10000)
print(rafsun.holder_name)
# rafsun.balance = 0  # X
# print(rafsun.__balance) # X
print(rafsun.get_balance())
rafsun.deposit(40000)
print(rafsun.get_balance())
rafsun.holder_name = 'boro vai'
print(rafsun.holder_name)
print(rafsun._branch)

# access private attribute forcefully
# print(dir(rafsun))
print(rafsun._Bank__balance)