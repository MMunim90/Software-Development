numbers = [12, 56, 98, 78, 56, 12, 26, 98]
person1 = ['kala chan', 'kaligong', 23, 'student']

# key value pair
# dictionary
# object
# hash table
# overlap with set

# dictionary structure = {key : value, key : value, key : value}
person = {'name': 'kala pakhi', 'address': 'kaligong', 'age': 23, 'job': 'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

person['language'] = 'python'
print(person)

person['name'] = 'sada pakhi'
print(person)

del person['age']
print(person)

# for this loop we get here only keys
# for item in person:
#     print(item)

# special dictionary looping
for key, value in person.items():
    print(key, ':', value)