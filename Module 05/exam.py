from random import *
class Exam:
    def __init__(self, examinee):
        self.examinee = examinee
        
    def attend_exam(self):
        print(f'Welcome {self.examinee}, for attending an exam!!!')
        print('Which subject exam do you want to participate? ')
        self.exam_subjects()
        sub = input()
        print('Choose your exam duration: ')
        self.available_exam_time()
        time = input()
        print(f'Wow {self.examinee} nice! Seems like your preparation is very good? Ok best of luck. Your time start now....')
        print(f'Subject: {sub} and Time: {time}')
    
    def exam_subjects(self):
        subjects = ['Bangla', 'English', 'Math', 'Physics', 'Chemistry', 'Biology']
        for i, sub in enumerate(subjects, start=1):
            print(i, '->', sub)
        return subjects
        
    def available_exam_time(self):
        time = ['2 hrs', '1 hrs', '30 min', '15 min', '5 min', '1 min']
        for i, t in enumerate(time, start=1):
            print(i, '->', t)
        return time
    
    def get_marks(self):
        print(f'Wow!!! {self.examinee}, You did outstanding. Your obtained mark\'s is: {randint(70, 100)}')
        
munim = Exam('munim')
# munim.exam_subjects()
# munim.available_exam_time()
munim.attend_exam()
# munim.get_marks()