num = int(input())
user_input = input().split()

numbers = []
for ch in user_input:
    numbers.append(int(ch))
    
freq = {}

total_remove = 0
    
for number in numbers:
    if number in freq:
        freq[number] += 1
    else:
        freq[number] = 1
        
    
for key, value in freq.items():
    if key < value:
        total_remove += (value - key)
    elif key > value:
        total_remove += value

print(total_remove)