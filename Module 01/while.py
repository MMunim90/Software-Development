# loop

# num = 1
# while num <= 10:
#     print(num)
#     num += 1


# break and continue

# num = 1
# while num <= 10:
#     if num == 3:
#         num += 1
#         continue
#     print(num)
#     num = num + 1
#     if num == 8:
#         break


num = 1
while num <= 10:
    num = num + 1
    if num % 2 == 1:
        continue
    print(num)