print("Object oriented programming is contain class and objects")

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.radius

    def perimeter(self):
        return self.radius * self.radius * 2

print("calling circle object")
c = Circle(5)
print("Area of circle",c.area())
print("Perimeter of circle",c.perimeter())




import numpy as np

name = "Janvi Parmar"
a1 = np.array([1,3,5,7,9,11,13,15])
mean = np.mean(a1)

print("Name of Author:", name)
print("Mean of given array:",mean)

# data types :
age = 18 #int
sum = 124.535 #float
name = "Janvi Parmar" #string etc...
