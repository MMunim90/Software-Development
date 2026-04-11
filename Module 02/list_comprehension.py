numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds = []
even = []
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
    elif num % 2 == 0 and num % 5 == 0:
        even.append(num)
print(odds)
print(even)

# odd_nums = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_nums)


players = ['sakib', 'mushfiq', 'mustafiz']
ages = [38, 37, 32]

age_combination = []
for player in players:
    print('players:', player)
    for age in ages:
        print(player, age)
        age_combination.append([player, age])
print(age_combination)


# age_combination2 = [(player,age) for player in players for age in ages]
age_combination2 = [[player,age] for player in players for age in ages]
print(age_combination2)