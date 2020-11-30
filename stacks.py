"""
STACK
- Last In First Out (LIFO) container
- Can Push on (to the top of the stack)
- Can Pop off (from the top of the stack)
- Can Peek (view the top of the stack)
- Backend store can be a Linked List or an Array
- Can be useful for implementing an Undo function on a program/app

"""

from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.ll = LinkedList()
        self.count = self.ll.count

    def push(self, value):
        self.ll.add_to_tail(value)
        self.count = self.ll.count

    def pop(self):
        popped_value = None
        if self.count > 0:
            popped_value = self.ll.tail.value
            self.ll.remove_tail()
            self.count = self.ll.count
        return popped_value

    def peek(self):
        peek_value = None
        if self.count > 0:
            peek_value = self.ll.tail.value
        return peek_value
