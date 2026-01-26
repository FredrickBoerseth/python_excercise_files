class Shape:
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, bot, side):
        self.bottom = bot
        self.side = side

    def calculate_perimeter(self):
        print((self.bottom * 2) + (self.side * 2))
    

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        print(self.side * 4)

    def change_size(self, negative_num):
        self.side = self.side + negative_num
        print(self.side)


# r1 = Rectangle(2, 4)
# s1 = Square(4)

# r1.calculate_perimeter()
# s1.calculate_perimeter()
# s1.change_size(-1)

# s1.calculate_perimeter()

# s1.what_am_i()
# r1.what_am_i()

class Horse:
    def __init__(self, name, sex, rider):
        self.name = name
        self.sex = sex
        self.rider = rider
        print("Composed")
    

class Rider:
    def __init__(self, name):
        self.name = name
        print("Rider created")


fred = Rider("Fred")
horsea = Horse("Horsea", "female", fred)

print(horsea.rider.name)