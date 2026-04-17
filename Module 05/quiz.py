class A:
    def __init__(self, value):
        value = 3
        self.value = value
    
    def change(self):
        self.value = 12
        

ans = []
a = A(13)
print(a.value)
ans.append(a.value)
print(a.value)
a.change()
print(a.value)
ans.append(a.value)
print(a.value)
ans.append(a.value)
print(a.value)
print(ans)