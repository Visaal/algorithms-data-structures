"""QUEUE
A collection that returns items in the same order that they were added

- First In First Out (FIFO)
- Enqueue to add an item to the queue
- Dequeue to remove the head item from the queue
- Peek to see what item is at the head of the queue
- Can implement using a Linked List or an Array
- Can have a Priority Queue
"""

from linked_list import LinkedList


class FifoQueue:
    def __init__(self):
        self.ll = LinkedList()
        self.size = self.ll.count

    def enqueue(self, value):
        self.ll.add_to_tail(value)
        self.size = self.ll.count

    def dequeue(self):
        dequeued_item = None
        if self.size > 0:
            dequeued_item = self.ll.head.value
            self.ll.remove_head()
            self.size = self.ll.count
        return dequeued_item

    def peek(self):
        head_item = None
        if self.size > 0:
            head_item = self.ll.head.value
        return head_item
