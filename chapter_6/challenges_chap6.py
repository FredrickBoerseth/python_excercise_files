# 1. print every character in the string "Camus"
the_string = "Camus"
x1 = the_string[0]
x2 = the_string[1]
x3 = the_string[2]
x4 = the_string[3]
x5 = the_string[4]
# print(x1, x2, x3, x4, x5)

# 2. collect two strings, insert them into the string "Yesterday I wrote a [response_one]. I sent it to [response two]!"
response_one = input("first response: ")
response_two = input("Second response: ")
the_string = "Yesterday I wrote a {}. I sent it to {}!".format(response_one, response_two)
# print(the_string)

# 3. use a method to make the string "aldous Huxley was born in 1894." grammaticaly correct by capitalising the first letter in the sentence.
string_to_fix = "aldous Huxley was born in 1894."
x = how_to_fix = string_to_fix.capitalize()
print(x)

# 4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: ["Where now?", "Who now?", "When now?"].
the_string = "Where now? Who now? When now? "
x = how_to_solve = the_string.split("? ")
print(x)

# 5. Take the list -> turn it into gramatiically correct string.
the_list =  ["The", "fox", "jumped", "over", "the", "fence", "."]

sentence = " ".join(the_list[:-1])
sentence = sentence + the_list[-1]

print(sentence)


# 6. replace every instance of s with a dollar sign
the_string = "A screaming comes across the sky."
the_replace_part = the_string.replace("s", "$")
print(the_replace_part)

# 7. indexing -> find the first m
the_string = "Hemingway"
the_string = the_string.index("m")
print(the_string)

# 8. find dialogue in your favorite book ( containing quotes and turn it into a string)
the_string = '"I draw primarily because it is vital for me, and also to convey ideas"'
print(the_string)

# 9. create the string "three three three" using concatenation and the againg using multiplication
startin_point = "three "

concatenate_shit = startin_point + startin_point + startin_point
print(concatenate_shit)

multiply_shit = startin_point * 3
print(multiply_shit)

# 10. slice shit
the_string_to_slice = "It was a bright cold day in april, and the clocks were striking thirteen."

working_out_index = the_string_to_slice.index(",")

even_more_work = the_string_to_slice[:working_out_index]

result = even_more_work
print(result)