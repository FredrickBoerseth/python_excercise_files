class Square:
    square_list =  []

    def __init__(self, measurement):
        self.measurement = measurement
        self.square_list.append(self.measurement)

    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.measurement, self.measurement, self.measurement, self.measurement)



testin = Square(29)
testin1 = Square(1)
print(Square.square_list)

print(testin)
print(testin1)

def my_func(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False
    
x = my_func(testin1, testin1)
print(x)

x = my_func(testin, testin1)
print(x)
