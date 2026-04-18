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
    
class Phone(Device):
    def __init__(self, brand, price, color, origin, model, os_version, memory, dual_sim):
        self.model = model
        self.os_version = os_version
        self.memory = memory
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
        
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self):
        return f'Brand: {self.brand}, Price: {self.price}, Color: {self.color}, Assembled in: {self.origin}, Model: {self.model}, OS version: {self.os_version}, RAM: {self.memory}, Dual-Sim: {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel
    
    def change_lens(self):
        pass
    
# inheritance
my_phone = Phone('Asus', 56000, 'Black', 'China', 'K323', 'Android 12', '12 GB', True)
# my_phone.phone_call()
# print(my_phone.brand)
print(my_phone)