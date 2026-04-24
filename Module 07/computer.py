class CPU:
    def __init__(self, cores, thread):
        self.cores = cores
        self.thread = thread
        
class RAM:
    def __init__(self, size, ddr, speed):
        self.size = size
        self.ddr = ddr
        self.speed = speed
        
class HardDrive:
    def __init__(self, capacity, gen):
        self.capacity = capacity
        self.gen = gen
        
# computer has a cpu
# computer has a ram
# computer has a hard drive 
class Computer:
    def __init__(self, cores, ram_size, hdd_capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hdd = HardDrive(hdd_capacity)
        
        
mac = Computer(8, 16, 512)