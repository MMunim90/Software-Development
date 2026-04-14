string = input()
 
count = 0
counter = 0
 
str = ""
list = []
 
for ch in string:
    if ch == 'R':
        count -= 1
        str += ch
    else:
        count += 1
        str += ch
    if count == 0:
        counter += 1
        list.append(str)
        str = ""   
print(counter)
for l in list:
    print(l)