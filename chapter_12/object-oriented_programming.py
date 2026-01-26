class Orange:
    def __init__(self, w, c):
        """weights are in oz""" 
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")


    def rot(self, days, temp):
        self.mold = days * temp


or1 = Orange(4, "light orange")
or2 = Orange(8, "dark orange")
or3 = Orange(14, "yellow")


print(or1) # location in memory
print(or1.weight)
print(or1.color)

# change value of instance / object
x = or1.weight = 100
y = or1.color = "light orange"
print(x)
print(y)

# moldy part
orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 9.8)
print(orange.mold)
