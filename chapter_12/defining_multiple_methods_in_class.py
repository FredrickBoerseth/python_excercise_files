class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length
    
    def change_size(self, w, l):
        self.width = w
        self.length = l
    
rec1 = Rectangle(10, 20)
print(rec1.area())
rec1.change_size(20, 40)
print(rec1.area())
