class Student:
    def __init__(self, name, student_class, id):
        self.name = name
        self.student_class = student_class
        self.id = id
        
    def __repr__(self):
        return f'Student name: {self.name}, class: {self.student_class}, id: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
        
    def __repr__(self):
        return f'Teacher\'s name: {self.name}, subject: {self.subject}'
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
        
    def enroll_student(self, name, fee):
        if fee < 10000:
            print('Not Enough Fee')
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 10000}'
        
    def __repr__(self):
        print('Welcome to', self.name)
        print('----------Our Teachers----------')
        for teacher in self.teachers:
            print(teacher)
        print('----------Our Students----------')
        for student in self.students:
            print(student)
        return '-----------Thank You-----------'
    
    
# alia = Student('Alia', 12, 12)
# ranbeer = Teacher('Ranbeer', 'Algorithm', 101)
# print(alia)
# print(ranbeer)


shikhi = School('Shikhi')
shikhi.enroll_student('alia', 8000)
shikhi.enroll_student('rita', 11000)
shikhi.enroll_student('babu', 18000)
shikhi.enroll_student('rahim', 10000)
shikhi.enroll_student('karim', 100000)

shikhi.add_teacher('Tom Cruise', 'Algorithm')
shikhi.add_teacher('Decap', 'DS')
shikhi.add_teacher('Aj', 'Database')

print(shikhi)