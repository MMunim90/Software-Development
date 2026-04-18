# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

# parent class
class Device:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
        
    def run(self):
        pass

class Laptop:
    def __init__(self, model, windows_version, memory, ssd):
       self.model = model
       self.windows_version = windows_version
       self.memory = memory
       self.ssd = ssd
    
    def coding(self):
        return f'learning python and practicing'
    
class Phone:
    def __init__(self, model, os_version, memory, dual_sim):
        self.model = model
        self.os_version = os_version
        self.memory = memory
        self.dual_sim = dual_sim
        
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel
    
    def change_lens(self):
        pass