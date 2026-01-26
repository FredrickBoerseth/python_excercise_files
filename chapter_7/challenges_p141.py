# 1. print each item in the following list:
the_list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for item in the_list:
    print(item)


# 2. print all the numbers from 25 - 50
for num in range(25, 51):
    print(num)

# 3. print each item in the list from the first challenge and their indexes.
for item in enumerate(the_list):
    print(item)

# 4. Write a program with an infinite loop ( with the option to type q to quit) and a list of numbers.
# Each time trough the loop ask the user to guess a number on the list and tell them eheter or not they
# guessed correctly.

# num_list = ["1", "2", "5", "6", "8"]
# while True:
#     print("Guess the number")
#     x = input("Guess a num: ")
#     if x == "q":
#         break
#     elif x in num_list:
#         print(True)
#     else:
#         print(False)


# 5. multiply all numbers in list with all in the secondou, andou appendou resulto tou a newo listo
list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
new_list = []

for i in list_1:
    for j in list_2:
        new_list.append(i+j)
print(new_list)