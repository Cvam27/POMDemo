class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Vehicle("School Volvo", 12, 50)
print(isinstance(School_bus, Bus))
