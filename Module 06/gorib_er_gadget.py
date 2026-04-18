class Laptop:
    def __init__(self, brand, price, model, color, windows_version, memory):
       self.brand = brand
       self.price = price
       self.model = model
       self.color = color
       self.windows_version = windows_version
       self.memory = memory
       
    def run(self):
        return f'Running {self.windows_version} on {self.brand} {self.model}'
    
    def coding(self):
        return f'learning python and practicing'
    
class Phone:
    def __init__(self, brand, price, model, color, os_version, memory, dual_sim):
        self.brand = brand
        self.price = price
        self.model = model
        self.color = color
        self.os_version = os_version
        self.memory = memory
        self.dual_sim = dual_sim
        
    def run(self):
        return f'Running {self.os_version} on {self.brand} {self.model}'
        
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self, brand, price, color, pixel):
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel
        
    def run(self):
        pass
    
    def change_lens(self):
        pass