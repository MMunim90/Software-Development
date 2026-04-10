# list, array, collection is same thing

# index = 0   1   2   3   4   5   6   7   8   9
number = [45, 56, 12, 89, 87, 32, 69, 59, 46, 93]
#index = -10  -9  -8  -7  -6  -5  -4  -3  -2  -1


# print(number[3])
# print(number[-7])

# print(number[3], number[-3])


# list( start : end )
# start from the start index and end stops before the end index
# print(number[2:6])
print(number[1:7])

# list(start : end : step)
print(number[1:7:1])
print(number[1:7:2])
print(number[2:7:-1])
print(number[7:2:-1])
print(number[7:2:-2])
print(number[4:])
print(number[:5])
print(number[:]) # shortcut to copy a list
print(number[::-1]) # shortcut to reverse a list