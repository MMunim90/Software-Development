# in, not, not in, is, is not
# >, <, >=, <=, ==, !==
# and, or

# a = 55
# if a > 33:
#     print('greater than 33')
# elif a > 5:
#     print('grater than 5')
#     print('koto besi ke jane')
# elif a == 5:
#     print('equal to 5')
# else:
#     print('less than 5')


# boss = False
# if boss is True:
#     print('tel er bakso niye astesi boss re tell dibo');
# else:
#     print('lunch er pore ashen')


# if boss is not True:
#     print('lunch er pore ashen')
# else:
#     print('tel er bakso niye astesi boss re tell dibo');


# nested condition
boss = False
coin = 'head'
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do something')
            if 8%2 == 0 and 5%2 == 1:
                print('8 is a even number')
else:
    print('you are loss not a boss')