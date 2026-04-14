class Calculator:
    brand = 'Casio EX 991'
    
    def add(self, num1, num2):
        return num1 + num2
    
    def deduct(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 // num2
    

calculate = Calculator()
sum = calculate.add(5, 6)
sub = calculate.deduct(5, 6)
mul = calculate.multiply(5, 6)
div = calculate.divide(30, 5)

print(sum, sub, mul, div)