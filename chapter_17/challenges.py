import re

# challenge 1

zen_o_py = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

x = re.findall("Dutch", zen_o_py, re.IGNORECASE)
print(x)


# challenge 2
the_string = "Arizona 479, 501, 870. California 209, 213, 650."

x = re.findall("\d", the_string)
print(x)

# challenge 3
the_sentence = "The ghost that says boo haunts the loo"

# get all words that end with double o.. oo

x = re.findall(".?oo", the_sentence)
print(x)