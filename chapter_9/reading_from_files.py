with open("st.txt", "r") as f:
    print(f.read())

# save contents from the prev. ex in a list

my_list = list()
with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)