# hw 1
num1 = int(input('give 1st number: '))
num2 = int(input('give 2nd number: '))
num3 = int(input('give 3rd number: '))

if num1 > num2 and num1 > num3:
    print('largest number is: ', num1)
elif num2 > num1 and num2 > num3:
    print('largest number is: ', num2)
else:
    print('largest number is: ', num3)
