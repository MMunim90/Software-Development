
# global variable
balance = 3000

# you can access global variable without using the global keyword but if you want to modify a global variable, you have to use the global keyword.

def buy_things(item, price):
    # local scope variable
    dream_phone = 'xphone'
    # print(dream_phone)
    # balance = 1500
    global balance
    print(f'previous balance: ', balance)
    # balance = balance
    balance = balance - price
    print(f'balance after buying {item}: ', balance)

# print(dream_phone)

buy_things('sunglass', 1000)
print('global balance after buy', balance)