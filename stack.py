# Experiment with python implementation of stack...not built in so list functions are modified
# LIFO  = Last In First Out

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        """ Comparing current list to an empty list. """
        return self.items == []

    def peek(self):
        """ Python allows you to reverse index lists using negative numbers. """
        return self.items[-1]

    def get_stack(self):
        return self.items

# Implementation
s = Stack()
print(s.get_stack())
s.push(1)
s.push(2)
print(s.get_stack())
s.pop()
print(s.get_stack())
s.push(1000)
print(s.peek())
