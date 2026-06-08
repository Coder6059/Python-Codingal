class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ob1 = vehicle(100, 1000)
print("The max speed of the vehicle is ", ob1.max_speed)
print("The mileage of the vehicle is ", ob1.mileage)
