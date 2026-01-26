# 1. create a list of your favourite musicians
my_favorite_musicians = ["Five finger death punch", "Avenged sevenfold"]

# 2. create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited
visited_Manila = (14.5995, 120.9842)
lived_Oslo = (59.9122, 10.7313)
lived_Trondheim = (64.4305, 10.3951)
visited_Alanya = (36.5444, 31.9954)

# 3. create a dictionary that contains different attributes about you: height, favourite color: favourite author, etc.
my_dict = {
    "height": "173 cm",
    "favourite color": "Black",
    "favorite author": "Bryan Peterson",
    "favorite music genre": "metalcore",
    "pasttime": ["drawing", "photography", "coding"],
    "favorite coding language": "Python 3"
}

# 4. write a program that lets the user ask our height, favourite colour, or favourite author, and returns the result from the dictionary you created in the previous challenge

print("height")
print("favourite color")
print("favourite author")
curiosities = input("What would you like to know?")
if curiosities in my_dict:
    stuff_to_print = my_dict[curiosities]
    print(stuff_to_print)
else:
    print("Notu foundu")

# 5. favourite musician and favorite songs by them, written with a dict

favourite_sounds_and_soundmakers = {
    "Five finger death punch": "Far from home",
    "Avenged Sevenfold": "Seize the day"

}

# 6. research sets, when would you use a set?
s2 = set() # create empty set
s3 = {} # create empty dict
s1 = {1, 2, 3, 4, 5}
s2 = {7, 8, 9}
s1.update([6, 7, 8], s2)
s1.discard(5)
print(s1)

# for å fjernes dupes og sammenlikne lister med hverandre

# for å se hvilke like verdier en liste har, eller ulike verdier