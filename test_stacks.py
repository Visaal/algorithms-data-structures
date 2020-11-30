"""
STACK
- Last In First Out (LIFO) container
- Can Push on (to the top of the stack)
- Can Pop off (from the top of the stack)
- Can Peek (view the top of the stack)
- Backend store can be a Linked List or an Array
- Can be useful for implementing an Undo function on a program/app

"""
import unittest
from stacks import Stack


class TestStack(unittest.TestCase):

    def test_stack_create(self):
        my_stack = Stack()
        self.assertEqual(0, my_stack.count)

    def test_stack_push_one_item(self):
        value = 5
        my_stack = Stack()
        my_stack.push(value)
        self.assertEqual(1, my_stack.count)
        self.assertEqual(5, my_stack.ll.tail.value)

    def test_stack_push_two_items(self):
        value1, value2 = 5, 8
        my_stack = Stack()
        my_stack.push(value1)
        self.assertEqual(1, my_stack.count)
        self.assertEqual(5, my_stack.ll.tail.value)
        my_stack.push(value2)
        self.assertEqual(2, my_stack.count)
        self.assertEqual(8, my_stack.ll.tail.value)

    def test_pop_one_item(self):
        value1 = 5
        my_stack = Stack()
        my_stack.push(value1)
        popped_item = my_stack.pop()
        self.assertEqual(5, popped_item)
        self.assertEqual(0, my_stack.count)

    def test_pop_no_items(self):
        my_stack = Stack()
        popped_item = my_stack.pop()
        self.assertEqual(0, my_stack.count)
        self.assertEqual(None, popped_item)

    def test_pop_multiple_items(self):
        value1, value2, value3 = 5, 8, 11
        my_stack = Stack()
        my_stack.push(value1)
        my_stack.push(value2)
        my_stack.push(value3)
        popped_item1 = my_stack.pop()
        popped_item2 = my_stack.pop()
        popped_item3 = my_stack.pop()
        self.assertEqual(0, my_stack.count)
        self.assertEqual(11, popped_item1)
        self.assertEqual(8, popped_item2)
        self.assertEqual(5, popped_item3)

    def test_peek_single_item(self):
        value1 = 5
        my_stack = Stack()
        my_stack.push(value1)
        peeked_item = my_stack.peek()
        self.assertEqual(1, my_stack.count)
        self.assertEqual(5, peeked_item)

    def test_peek_no_item(self):
        my_stack = Stack()
        peeked_item = my_stack.peek()
        self.assertEqual(0, my_stack.count)
        self.assertEqual(None, peeked_item)

    def test_peek_multiple_items(self):
        value1, value2, value3 = 5, 8, 11
        my_stack = Stack()
        my_stack.push(value1)
        my_stack.push(value2)
        my_stack.push(value3)
        peeked_item = my_stack.peek()
        self.assertEqual(3, my_stack.count)
        self.assertEqual(11, peeked_item)


if __name__ == '__main__':
    unittest.main()
