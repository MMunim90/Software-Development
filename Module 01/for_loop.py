# numbers = [5, 10, 15, 20, 25]

# sum = 0
# for num in numbers:
#     print(num)
#     sum = sum + num
#     if sum > 20:
#         print('bigger sum', sum)
# print(sum)


# text = 'pagla howar'

# for char in text:
#     print(char)


# range
# for i in range(1, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)


# enumerate

fruits = ['apple', 'banana', 'mango']

# for index, value in enumerate(fruits):
#     print(index, value)

for index, value in enumerate(fruits, start=1):
    print(index, value)