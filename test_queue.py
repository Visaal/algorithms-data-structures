"""QUEUE
A collection that returns items in the same order that they were added

- First In First Out (FIFO)
- Enqueue to add an item to the queue
- Dequeue to remove the head item from the queue
- Peek to see what item is at the head of the queue
- Can implement using a Linked List or an Array
- Can have a Priority Queue
"""

import unittest
from queue import FifoQueue


class TestQueue(unittest.TestCase):

    def test_queue_create(self):
        queue = FifoQueue()
        self.assertEqual(0, queue.size)

    def test_enqueue_one_item(self):
        value = 5
        queue = FifoQueue()
        queue.enqueue(value)
        self.assertEqual(1, queue.size)
        self.assertEqual(5, queue.ll.head.value)

    def test_enqueue_two_items(self):
        value1, value2 = 5, 10
        queue = FifoQueue()
        queue.enqueue(value1)
        queue.enqueue(value2)
        self.assertEqual(2, queue.size)
        self.assertEqual(5, queue.ll.head.value)
        self.assertEqual(10, queue.ll.tail.value)

    def test_enqueue_three_items(self):
        value1, value2, value3 = 5, 10, 15
        queue = FifoQueue()
        queue.enqueue(value1)
        queue.enqueue(value2)
        queue.enqueue(value3)
        self.assertEqual(3, queue.size)
        self.assertEqual(5, queue.ll.head.value)
        self.assertEqual(15, queue.ll.tail.value)


    def test_dequeue_one_item_on_queue(self):
        value = 5
        queue = FifoQueue()
        queue.enqueue(value)
        removed_item = queue.dequeue()
        self.assertEqual(0, queue.size)
        self.assertEqual(5, removed_item)

    def test_dequeue_no_items_on_queue(self):
        queue = FifoQueue()
        removed_item = queue.dequeue()
        self.assertEqual(0, queue.size)
        self.assertEqual(None, removed_item)

    def test_dequeue_multiple_items_on_queue(self):
        value1, value2, value3 = 5, 10, 15
        queue = FifoQueue()
        queue.enqueue(value1)
        queue.enqueue(value2)
        queue.enqueue(value3)
        removed_item1 = queue.dequeue()
        removed_item2 = queue.dequeue()
        removed_item3 = queue.dequeue()
        self.assertEqual(0, queue.size)
        self.assertEqual(5, removed_item1)
        self.assertEqual(10, removed_item2)
        self.assertEqual(15, removed_item3)

    def test_peek_one_item_one_queue(self):
        value = 5
        queue = FifoQueue()
        queue.enqueue(value)
        peeked_value = queue.peek()
        self.assertEqual(1, queue.size)
        self.assertEqual(5, peeked_value)

    def test_peek_no_items_on_queue(self):
        queue = FifoQueue()
        peeked_value = queue.peek()
        self.assertEqual(0, queue.size)
        self.assertEqual(None, peeked_value)

    def test_peek_multiple_items_on_queue(self):
        value1, value2, value3 = 5, 10, 15
        queue = FifoQueue()
        queue.enqueue(value1)
        queue.enqueue(value2)
        queue.enqueue(value3)
        peeked_item = queue.peek()
        self.assertEqual(3, queue.size)
        self.assertEqual(5, peeked_item)


if __name__ == '__main__':
    unittest.main()
