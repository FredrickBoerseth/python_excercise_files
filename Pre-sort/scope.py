# writing to a global variable from a function

x = 100

def ex():
    global x
    x += 1
    return x

result = ex()
print(result)