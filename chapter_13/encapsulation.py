class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length
    

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients shouldn't use this
        pass


# Rectangle clasu
new_r = Rectangle(2, 3)
print(new_r.area())
    

# data clasu
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

