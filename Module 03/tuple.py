def multiple():
    return 3, 4
# print(multiple())

things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'

# print(things)
# print(type(things))

# print(things[0])
# print(things[-2])
# print(things[3:6])


# if 'phone' in things:
#     print('exists')
    
# for item in things:
#     print(item)


# things[0] = 'wagon'  # this line showing error because tuple are immutable
# print(things)

# print(len(things))

items = ('book', 'monitor', 'clock')


mega = ([2, 3, 4], [5, 6, 7], [8, 9, 1])
# print(mega)
# print(type(mega))
# mega[0] = [1, 6, 5]  # this line showing error because tuple are immutable
# print(mega[0])

mega[0][1] = 7
print(mega)