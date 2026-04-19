class Book:
    def __init__(self, name):
        self.name = name
        
    def read(self):
        pass
    
    def write(self):
        raise NotImplementedError
        
class Physics(Book):
    def __init__(self, name, lab):
        self.lab = lab
        super().__init__(name)
        
    def read(self):
        pass
        
    def write(self):
        print('Solving some problem on physics vector chapter')
        
class Student:
    def __init__(self, name):
        self.name = name
        
topon = Physics('topon', True)

print(issubclass(Physics, Book))
print(issubclass(Student, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

topon.read()
topon.write()