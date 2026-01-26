# # string stuff
# name = "Ted"
# for character in name:
#     print(character)

# # listing stuff
# shows = ["GOT", "Narcos", "Vice"]
# for show in shows:
#     print(show)

# # tuple stuff
# coms = ("A. Development", "Friends", "Always Sunny")
# for show in coms:
#     print(show)

# # dictionairy
# people = {"G. Bluth II": "A. Development",
#           "Barney": "HIMYM", "Dennis": "Always Sunny"}

# for character in people:
#     print(character)


tv = ["GOT", "Narcos", "Vice"]
i = 0

for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

# because its common to access each item and its index, python has a another way to do this:

tv = ["GOT", "Narcos", "Vice"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

# take all strings from two different lists, capitalize each char, and putem into new list

tv = ["GOT", "Narcos", "Vice"]
coms = ("A. Development", "Friends", "Always Sunny")
all_shows =  []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

for i in range(1, 11):
    print(i)

