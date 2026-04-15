class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            
    def withdraw(self, amount):
        if self.balance > amount:
            if amount < self.min_withdraw:
                print(f'You cannot withdraw below {self.min_withdraw} taka')
            elif amount > self.max_withdraw:
                print(f'You cannot withdraw more than {self.max_withdraw} taka')
            else:
                self.balance -= amount
                print(f'Your current balance after withdraw is: {self.check_balance()} taka')
        else:
            print(f'Your current balance is lower than {amount} taka')
            
brac = Bank(150000)
# brac.withdraw(25)
# brac.withdraw(1000000000000)
# brac.withdraw(100000)
# my_current_balance = brac.check_balance()
# print(my_current_balance)


dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.check_balance())