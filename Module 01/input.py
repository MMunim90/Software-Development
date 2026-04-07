# print('Now I need money')
# input()

# input('Give me some money: ')

# money = input('Give me some money: ')
# print("here is your money: ", money)
# print(f"this is your money: {money}")


first_money = input('kodom ali, dosto kichu taka dey: ')
print(type(first_money))
# by default the input from user will be string type
second_money = input('peyara begum, apu kichu taka dey: ')
print('money I got: ', first_money, ' and ', second_money)
first_money_int = int(first_money)
second_money_int = int(second_money)
# print(type(first_money_int))
# total = first_money + second_money
total_money = first_money_int + second_money_int
print('total money I got: ', total_money)