class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        final_fare = base_fare + (base_fare * 0.10)
        return final_fare

school_bus = Bus("School Bus", 50)
print(f"Total fare for the {school_bus.name} is: INR {school_bus.fare()}")