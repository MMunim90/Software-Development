# XYZ Poribohon

class Company:
    def __init__(self, name, address, owner):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        self.fare = []
        
class Driver:
    def __init__(self, name, license, age, experience):
        self.name = name
        self.license = license
        self.age = age
        self.experience = experience
        
class Counter:
    def __init__(self):
        pass
    
    def purchase_a_ticket(self, start, destination, seat_type):
        pass

class Passenger:
    pass

class Supervisor:
    pass


lal_mia = Driver('lalu', '1324234', 35, 5)