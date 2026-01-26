from math import pi

class Apple:
    def __init__(self, weight, color, stem, clean):
        self.weight = weight
        self.color = color
        self.stem = stem
        self.clean = clean
        print("Apple synthesized")

a1 = Apple(140, "yellow", True, "True")


class Circle:
    def __init__(self):
        print("circle created")

    def area(self, radius):
        area = pi * pow(radius, 2)
        return "{} cm^2".format(area)
    
c1 = Circle()
print(c1.area(2))


class Triangle:
    def __init__(self):
        print("Triangle Created")

    def area(self, bot, height):
        area = (bot * height)/2
        return "{} cm^2".format(area)
    
t1 = Triangle()
print(t1.area(6, 4))


class Hexagon:
    def __init__(self):
        print("Hexagon created")

    def calculate_perimiter(self, one_side):
        return one_side * 6
    
h1 = Hexagon()
print(h1.calculate_perimiter(3))