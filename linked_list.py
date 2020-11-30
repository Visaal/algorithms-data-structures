""""
LINKED LISTS

Built of nodes, a node is a simple structure that holds an item of data along with a pointer to another node

Linked lists are a single chain of nodes
They have a starting point which is called the Head (there is a pointer to the Head)
The end node is known as the Tail (there is a pointer to the Tail)
The LL supported operations are Add, Remove, Find, Enumerate

Key benefit is efficient insertion
If adding a node at the beginning you are just changing the head pointer
If using an array you would have to shift all elements to the right
Potentially if array is full you would have to copy to a larger array from the smaller one
This way when adding a node the operation expense is always the same

Starting with an empty list, Head and Tail are null
first step is to add a node as the head, as there is only one node it is also the tail
Adding a second node just involves allocating a new node and point the Head to it and pointing
its next pointer to the previous node. No need to update the Tail pointer as adding a node to the
start of the list


methods to implement:
- Add to Head (checking if adding to an empty list or existing one)
- Add to Tail (check if adding to an empty list or existing one)
- Remove First node
- Remove Last node
- Enumerate - use a generator
- Clear - remove all nodes from the linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_head(self, value):
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
        self.count += 1

    def add_to_tail(self, value):
        if self.count == 0:
            self.tail = Node(value)
            self.head = self.tail
        else:
            new_node = Node(value)
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        self.count += 1

    def remove_head(self):
        if self.count == 0:
            return
        elif self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next_node.previous_node = None
            self.head = self.head.next_node
        self.count -= 1

    def remove_tail(self):
        if self.count == 0:
            return
        elif self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.previous_node.next_node = None
            self.tail = self.tail.previous_node
        self.count -= 1

    def enumerate(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
