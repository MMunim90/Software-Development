# default parameter

def sum(num1, num2, num3=0, num4=0, num5=0):
    result = num1 + num2 + num3 + num4 + num5
    return result

# total = sum(99, 11, 5)
# print('total: ', total)

# args
# def all_sum(*numbers):
#     print(numbers)
#     sum = 0
#     for num in numbers:
#         sum += num
#     return sum
    
# total = all_sum(45, 46, 89, 11, 81)
# print('all sum: ', total)


def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum
        
total = all_sum(45, 46, 34, 43, 54)
print('all sum: ', total)