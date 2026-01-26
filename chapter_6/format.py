x = "William {}".format("Faulkner")
print(x)

author = "William Faulkner"
year_born = "1897"

x = "{} was born in {}.".format(author, year_born)
print(x)


n1 = input("Enter a noun: ")
v = input("Enter av verb: ")
adj = input("Enter an adj: ")
n2 = input("Enter a noun: ")

r = """The {} {} the {} {}
    """.format(n1, v, adj, n2)

print(r)
