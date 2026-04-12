name = 'sakib khan'
name1 = 'sakib\'s khan' # escape
name2 = "sakib khan"
# multiline string
name3 = """
    number one
    sakib khan
"""

print(name)
print(name1)
print(name2)
print(name3)

# list mutable, mutable means changeable
# string is a sequence of character
# string immutable, immutable means you can not change it

for char in name2:
    print(char)

print(name2[9])

print(name2[1:6])

print(name2[-3])

print(name2[::-1])

# name2[0] = 'R' # this line gives ans error , because string are immutable
print(name2)

if 'khan' in name2:
    print('exists')
if 'hati' in name2:
    print('exists')
else:
    print('not exists')
    
print(name2.upper())
print(name2.lower())
print(name2.capitalize())
print(name2.title())