# reverse a string using a stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    
# numero uno

the_stack = Stack()
the_word = "yesterday"
for char in the_word:
    the_stack.push(char)

reversed = ""

for x in range(len(the_stack.items)):
    reversed += the_stack.pop()

print(reversed)

# dos
# create new stack with this list [1, 2, 3, 4, 5] reversed

new_stack = Stack()
my_list = []
new_list = []

for i in range(1, 6):
    my_list.append(i)

for stuff in range(len(my_list)):
    new_list.append(my_list.pop())

print(new_list)