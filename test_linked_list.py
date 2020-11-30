import unittest
from linked_list import Node, LinkedList


class TestLinkedListNode(unittest.TestCase):

    def test_node(self):
        node = Node(3)
        self.assertEqual(3, node.value)
        self.assertEqual(None, node.next_node)
        self.assertEqual(None, node.previous_node)

    def test_node_link_node_next_node(self):
        n1 = Node(3)
        n2 = Node(5)
        n1.next_node = n2
        self.assertEqual(n2, n1.next_node)
        self.assertEqual(5, n1.next_node.value)

    def test_node_link_node_previous_node(self):
        n1 = Node(3)
        n2 = Node(5)
        n2.previous_node = n1
        self.assertEqual(n1, n2.previous_node)
        self.assertEqual(3, n2.previous_node.value)


class TestLinkedList(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_linked_list_add_to_head(self):
        ll = LinkedList()
        ll.add_to_head(3)
        self.assertEqual(3, ll.head.value)
        self.assertEqual(3, ll.tail.value)
        self.assertEqual(None, ll.head.next_node)
        self.assertEqual(None, ll.head.previous_node)
        self.assertEqual(1, ll.count)

    def test_linked_list_add_to_head_two_nodes(self):
        ll = LinkedList()
        ll.add_to_head(5)
        ll.add_to_head(3)
        # 3 <-> 5
        self.assertEqual(3, ll.head.value)
        self.assertEqual(5, ll.tail.value)
        self.assertEqual(5, ll.head.next_node.value)
        self.assertEqual(3, ll.tail.previous_node.value)
        self.assertEqual(2, ll.count)

    def test_linked_list_add_to_head_three_nodes(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        # 3 <-> 5 <-> 7
        self.assertEqual(3, ll.head.value)
        self.assertEqual(5, ll.head.next_node.value)
        self.assertEqual(7, ll.head.next_node.next_node.value)
        self.assertEqual(7, ll.tail.value)
        self.assertEqual(5, ll.tail.previous_node.value)
        self.assertEqual(3, ll.tail.previous_node.previous_node.value)
        self.assertEqual(3, ll.count)

    def test_linked_list_add_to_tail(self):
        ll = LinkedList()
        ll.add_to_tail(3)
        self.assertEqual(3, ll.head.value)
        self.assertEqual(3, ll.tail.value)
        self.assertEqual(None, ll.head.next_node)
        self.assertEqual(None, ll.tail.previous_node)
        self.assertEqual(1, ll.count)

    def test_linked_list_add_to_tail_two_nodes(self):
        ll = LinkedList()
        ll.add_to_tail(3)
        ll.add_to_tail(5)
        # 3 <-> 5
        self.assertEqual(3, ll.head.value)
        self.assertEqual(5, ll.tail.value)
        self.assertEqual(5, ll.head.next_node.value)
        self.assertEqual(3, ll.tail.previous_node.value)
        self.assertEqual(2, ll.count)

    def test_linked_list_add_to_tail_three_nodes(self):
        ll = LinkedList()
        ll.add_to_tail(3)
        ll.add_to_tail(5)
        ll.add_to_tail(7)
        # 3 <-> 5 <-> 7
        self.assertEqual(3, ll.head.value)
        self.assertEqual(5, ll.head.next_node.value)
        self.assertEqual(7, ll.head.next_node.next_node.value)
        self.assertEqual(7, ll.tail.value)
        self.assertEqual(5, ll.tail.previous_node.value)
        self.assertEqual(3, ll.tail.previous_node.previous_node.value)
        self.assertEqual(3, ll.count)

    def test_linked_list_remove_head_single_node_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.remove_head()
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_linked_list_remove_head_two_node_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.remove_head()
        # BEFORE: 5 <-> 7
        # AFTER: 7
        self.assertEqual(7, ll.head.value)
        self.assertEqual(7, ll.tail.value)
        self.assertEqual(1, ll.count)

    def test_linked_list_remove_head_three_node_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        ll.remove_head()
        # BEFORE: 3 <-> 5 <-> 7
        # AFTER: 5 <-> 7
        self.assertEqual(5, ll.head.value)
        self.assertEqual(7, ll.tail.value)
        self.assertEqual(7, ll.head.next_node.value)
        self.assertEqual(5, ll.tail.previous_node.value)
        self.assertEqual(None, ll.head.previous_node)
        self.assertEqual(None, ll.tail.next_node)
        self.assertEqual(2, ll.count)

    def test_linked_list_remove_head_empty_list(self):
        ll = LinkedList()
        ll.remove_head()
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_linked_list_remove_head_clear_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        ll.remove_head()
        ll.remove_head()
        ll.remove_head()
        # BEFORE: 3 <-> 5 <-> 7
        # AFTER:
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_linked_list_remove_tail_single_node_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.remove_tail()
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_linked_list_remove_tail_two_node_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.remove_tail()
        # BEFORE: 5 <-> 7
        # AFTER: 5
        self.assertEqual(5, ll.head.value)
        self.assertEqual(5, ll.tail.value)
        self.assertEqual(None, ll.head.next_node)
        self.assertEqual(None, ll.tail.previous_node)
        self.assertEqual(1, ll.count)

    def test_linked_list_remove_tail_three_node_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        ll.remove_tail()
        # BEFORE: 3 <-> 5 <-> 7
        # AFTER: 3 <-> 5
        self.assertEqual(3, ll.head.value)
        self.assertEqual(5, ll.head.next_node.value)
        self.assertEqual(5, ll.tail.value)
        self.assertEqual(3, ll.tail.previous_node.value)
        self.assertEqual(2, ll.count)

    def test_linked_list_remove_tail_empty_list(self):
        ll = LinkedList()
        ll.remove_tail()
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_linked_list_remove_tail_clear_list(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        ll.remove_tail()
        ll.remove_tail()
        ll.remove_tail()
        # BEFORE: 3 <-> 5 <-> 7
        # AFTER:
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

    def test_enumerate(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        # 3 <-> 5 <-> 7
        generator = ll.enumerate()
        self.assertEqual(3, next(generator).value)
        self.assertEqual(5, next(generator).value)
        self.assertEqual(7, next(generator).value)

    def test_linked_list_clear(self):
        ll = LinkedList()
        ll.add_to_head(7)
        ll.add_to_head(5)
        ll.add_to_head(3)
        ll.clear()
        self.assertEqual(None, ll.head)
        self.assertEqual(None, ll.tail)
        self.assertEqual(0, ll.count)

if __name__ == '__main__':
    unittest.main()
