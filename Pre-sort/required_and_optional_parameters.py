def f(x=2):
    return x**x
 
def add_it(x, y=10):        # ved bruk av både valgfrie, og parameter som kreves må de valgfrie komme sist i rekken 
    return x + y


print(f())
print(f(4))

result = add_it(2)
print(result)
