from math import pow
class Shape():
    def __init__(self, height: float, width: float, radius: float):
        self.height = height
        self.width = width
        self.radius = radius

    def perimeter(self):
        print(f"=> Perimeter: {(self.height + self.width)*2}")

    def area(self):
        print(f"=> Perimeter: {self.height * self.width}")

    def area_circle(self):
        print(f"=> Area: {pow(self.radius, 2) * 3.14}")

    def perimeter_circle(self):
        print(f"=> Perimeter: {self.radius * 2 * 3.14}")

type_shape = input("Shape (rectangle|circle): ")
if type_shape == "circle":
    shape_radius = float(input("Input radius: "))
    Shape(0,0,shape_radius).area_circle()
    Shape(0,0,shape_radius).perimeter_circle()

elif type_shape == "rectangle":
    shape_height = float(input("Input height: "))
    shape_width = float(input("Input width: "))
    Shape(shape_height,shape_width,0).perimeter()
    Shape(shape_height,shape_width,0).area()
    
else:
    print("Invalid")