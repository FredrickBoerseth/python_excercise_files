# lage en klasse uten noen referanser

class Pencil:
    def __init__(self, brand, hardness):
        self.brand = brand
        self.hardness = hardness
        print("Pencil added!")

    def broken(self):
        return "brand: {}, hardness: {} isu brokenu".format(self.brand, self.hardness)

one_pencil = Pencil("Faber-Castell", "HB")
two_pencil = Pencil("Staedtler", "2B")
three_pencil = Pencil("Derwent", "2H")


one = one_pencil.hardness
one_ = one_pencil.brand
print(one)
print(one_)

four = Pencil("test", "3H")
x = four.broken()
print(x)


