exam_number = int(input())

if exam_number <= 100 and exam_number >= 80:
    print('You got A+')
elif exam_number <= 79 and exam_number >= 70:
    print('You got A')
elif exam_number <= 69 and exam_number >= 60:
    print('You got A-')
elif exam_number <= 59 and exam_number >= 50:
    print('You got B')
elif exam_number <= 49 and exam_number >= 40:
    print('You got C')
elif exam_number <= 39 and exam_number >= 33:
    print('You got D')
else:
    print('Opps! You are fail, Better Luck Next Time')