def full_name(first, last):
    name = f'full name is: {first} {last}'
    return name

# take parameter in order (serial wise)
# name = full_name('Alu', 'kodu')
name = full_name(last='kodu', first='alu')
# print(name)

# def famous_name(first, last, title, addition):
#     name = f'{title} {first} {last}'
#     return name

# name = famous_name(first='Taher', last='Ali', title='hujur', addition='taheri')
# print(name)


# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f'{first} {last}'
    # print(addition)
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='taher', last='ali', title='hujur', title2='halim', last2='khamu', addition='shayokh')
print(name)

# def function_name(num1, num2, *args, **kargs):


# return multiple thing from an array
def a_lot(num1, num2):
    sum = num1 + num2
    multi = num1 * num2
    remain = num1 - num2
    # return sum, multi, remain  # (return tuple)
    return [sum, multi, remain]  # (return list)

everything = a_lot(55, 21)
print(everything)