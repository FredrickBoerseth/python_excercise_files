# s2 = set() # create empty set
# s3 = {} # create empty dict
# s1 = {1, 2, 3, 4, 5}
# s2 = {7, 8, 9}
# s1.update([6, 7, 8], s2)
# s1.discard(5)
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# intersection stuffs
s4 = s1.intersection(s2, s3) # får alle like verdier i s1 og s2 og s3
print(s4)

# difference stuffs
s5 = s1.difference(s2) # hvilke verdier er i s1, men ikke s2
print(s5)

# symmetric difference
s6 = s2.symmetric_difference(s1)
print(s6)

# operations
l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
l3 = set(l1)
print(l2)
print(l3)

employees = ["Corey", "Jim", "Steven", "April", "Judy", "Jenn", "John", "Jane"]

gym_members = ["April", "John", "Corey"]

developers = ["Judy", "Corey", "Steven", "Jane", "April"]

# gym mem, and devs
result = set(gym_members).intersection(developers)
print(result)

# not gym mem, and devs

result = set(employees).difference(gym_members, developers)
print(result)
