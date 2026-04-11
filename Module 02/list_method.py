numbers = [12, 45, 98, 68]
numbers.append(56)
print(numbers)
numbers.insert(2, 71)
numbers.insert(0, 91)
print(numbers)

# if number not found in the list it gives an error
# numbers.remove(98)
# that's why u should use remove method like this way
if 98 in numbers:
    numbers.remove(98)
# numbers.remove(8)
if 8 in numbers:
    numbers.remove(8)
print(numbers)

last = numbers.pop()
print(last, numbers)

# worst approach
# index = numbers.index(45)
# index = numbers.index(5)

# best approach
if 5 in numbers:
    index = numbers.index(5)
    print(index)
if 45 in numbers:
    index = numbers.index(45)
    print(index)
    
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)