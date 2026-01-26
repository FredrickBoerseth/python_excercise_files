# creating a dictionary
my_dict = dict()
my_dict = {}

fruits = {
    "Apple": "Red",
    "banana": "Yellow"
}
print(fruits)

facts = dict()

# adding key value pair to a dictionary after it is createdd

# add a value
facts["code"] = "fun"
# look up a key
x = facts["code"]
print(x)

# add a value
facts["Bill"] = "Gates"
# look up a key
x = facts["Bill"]
print(x)

# add a value
facts["founded"] = 1776
# look up a key
x = facts["founded"]
print(x)

# checking if key exists in dictionary
bill = dict({"Bill Gates": "charitable"})
x = "Bill Gates" in bill
print(x)

x = "Bill Doors" not in bill
print(x)

x = "Selena Gomez" in bill
print(x)

# checking if value is present in dictionary
x = "charitable" in bill # comes up as false, doesnt wok
print(x)


# delete a key value pair
books = {
    "Dracula": "Stoker",
    "1984": "Orwell",
    "The Trial": "Kafka"
}

print(books)
del books["The Trial"]
print(books)