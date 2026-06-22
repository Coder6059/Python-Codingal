import math

class Circle:
    def __init__(self, radius):
        
        self.radius = radius

    def area(self):
        
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        
        return 2 * math.pi * self.radius



try:
    
    user_radius = float(input("Enter the radius of the circle: "))
    
    if user_radius < 0:
        print("Radius cannot be negative. Please enter a valid positive number.")
    else:
        
        my_circle = Circle(user_radius)
        
       
        print(f"\nResults for a circle with radius {user_radius}:")
        print(f"Area: {my_circle.area():.2f}")
        print(f"Perimeter: {my_circle.perimeter():.2f}")

except ValueError:
    print("Invalid input! Please enter a numerical value.")