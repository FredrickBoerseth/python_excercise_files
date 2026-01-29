def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))


## idea for program
## anagram that check the word given, crosscheks it with a file of words
# basically another version of this one