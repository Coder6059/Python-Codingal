# Finished in class since we had time
class Mahindra():
    def model(self):
        print("Mahindra 7XO")
    
    def color(self):
        print("Ruby Velvet")

    def variant(self):
        print("Petrol")

class Hyundai():
    def model(self):
        print("Hyundai Creta")
    
    def color(self):
        print("Polar White")

    def variant(self):
        print("Petrol")

class Kia():
    def model(self):
        print("Kia (All New) Seltos")
    
    def color(self):
        print("Aurora Black")

    def variant(self):
        print("Petrol")

obj_1 = Mahindra()
obj_2 = Hyundai()
obj_3 = Kia()
for car in(obj_1, obj_2, obj_3):
    car.model()
    car.color()
    car.variant()