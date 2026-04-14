num = int(input())
user_input = input().split()

half = lambda num : num/2

numbers = []
count = 0

for number in user_input:
    if number != " ":
        n = int(number)
        numbers.append(n)
    
all_even = True

while all_even != False:
    for number in numbers:
        if number % 2 != 0:
            all_even = False
            break
    if all_even == False:
        break
    numbers = list(map(half, numbers))
    count += 1
    
print(count)

