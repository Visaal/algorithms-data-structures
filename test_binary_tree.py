import unittest
from binary_tree import Node, BinaryTree


class TestNode(unittest.TestCase):

    def test_node(self):
        n = Node(4)
        self.assertEqual(4, n.value)
        self.assertEqual(None, n.left_child)
        self.assertEqual(None, n.right_child)

    def test_node_left_child(self):
        n1 = Node(4)
        n2 = Node(2)
        n1.left_child = n2
        self.assertEqual(n2, n1.left_child)
        self.assertEqual(2, n1.left_child.value)

    def test_node_right_child(self):
        n1 = Node(4)
        n2 = Node(6)
        n1.right_child = n2
        self.assertEqual(n2, n1.right_child)
        self.assertEqual(6, n1.right_child.value)


class TestBinaryTree(unittest.TestCase):

    def test_binary_tree_create(self):
        bt = BinaryTree()
        self.assertEqual(None, bt.root)
        self.assertEqual(0, bt.count)

    def test_binary_tree_add_root_node(self):
        bt = BinaryTree()
        bt.add_node(4)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(1, bt.count)
        self.assertEqual(None, bt.root.left_child)
        self.assertEqual(None, bt.root.right_child)

    #     4
    #    /
    #   2
    def test_binary_tree_add_second_smaller_node(self):
        bt = BinaryTree()
        bt.add_node(4)
        bt.add_node(2)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(None, bt.root.right_child)
        self.assertEqual(2, bt.count)

    #        4
    #       /
    #      3
    #     /
    #    2
    #   /
    #  1
    def test_binary_tree_add_three_smaller_node(self):
        bt = BinaryTree()
        bt.add_node(4)
        bt.add_node(3)
        bt.add_node(2)
        bt.add_node(1)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(3, bt.root.left_child.value)
        self.assertEqual(2, bt.root.left_child.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.left_child.value)
        self.assertEqual(None, bt.root.right_child)
        self.assertEqual(4, bt.count)

    #        4
    #         \
    #          6
    #           \
    #            8
    #             \
    #              10
    def test_binary_tree_add_three_larger_nodes(self):
        bt = BinaryTree()
        bt.add_node(4)
        bt.add_node(6)
        bt.add_node(8)
        bt.add_node(10)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(6, bt.root.right_child.value)
        self.assertEqual(8, bt.root.right_child.right_child.value)
        self.assertEqual(10, bt.root.right_child.right_child.right_child.value)
        self.assertEqual(None, bt.root.left_child)
        self.assertEqual(4, bt.count)

    #     4
    #    / \
    #   2   6
    def test_binary_tree_add_smaller_and_larger_nodes(self):
        bt = BinaryTree()
        bt.add_node(4)
        bt.add_node(6)
        bt.add_node(2)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(6, bt.root.right_child.value)
        self.assertEqual(3, bt.count)

    #        4
    #      /   \
    #     2     6
    #      \   / \
    #       3 4   8
    #            / \
    #           7   12
    def test_binary_tree_multiple_smaller_and_larger_nodes(self):
        bt = BinaryTree()
        bt.add_node(4)
        bt.add_node(2)
        bt.add_node(6)
        bt.add_node(3)
        bt.add_node(4)
        bt.add_node(8)
        bt.add_node(7)
        bt.add_node(12)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(6, bt.root.right_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(4, bt.root.right_child.left_child.value)
        self.assertEqual(8, bt.root.right_child.right_child.value)
        self.assertEqual(7, bt.root.right_child.right_child.left_child.value)
        self.assertEqual(12, bt.root.right_child.right_child.right_child.value)
        self.assertEqual(8, bt.count)

    def test_left_or_right_child_smaller_value(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(3)
        bt.root.right_child = Node(7)
        result = bt._left_or_right_child(bt.root, 2)
        self.assertEqual(bt.root.left_child, result)

    def test_left_or_right_child_larger_value(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(3)
        bt.root.right_child = Node(7)
        result = bt._left_or_right_child(bt.root, 5)
        self.assertEqual(bt.root.right_child, result)

    def test_left_or_right_child_equal_value(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(3)
        bt.root.right_child = Node(7)
        result = bt._left_or_right_child(bt.root, 4)
        self.assertEqual(bt.root.right_child, result)

    def test_left_or_right_child_no_smaller_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.right_child = Node(7)
        result = bt._left_or_right_child(bt.root, 2)
        self.assertEqual(None, result)

    def test_left_or_right_child_no_larger_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(3)
        result = bt._left_or_right_child(bt.root, 5)
        self.assertEqual(None, result)

    def test_add_node_to_parent_smaller_node(self):
        bt = BinaryTree()
        node = Node(4)
        bt._add_node_to_parent(node, 3)
        self.assertEqual(3, node.left_child.value)
        self.assertEqual(None, node.right_child)

    def test_add_node_to_parent_larger_node(self):
        bt = BinaryTree()
        node = Node(4)
        bt._add_node_to_parent(node, 5)
        self.assertEqual(5, node.right_child.value)
        self.assertEqual(None, node.left_child)

    def test_add_node_to_parent_equal_node(self):
        bt = BinaryTree()
        node = Node(4)
        bt._add_node_to_parent(node, 4)
        self.assertEqual(4, node.right_child.value)
        self.assertEqual(None, node.left_child)

    def test_determine_node_to_add_to_root_only_smaller_value(self):
        bt = BinaryTree()
        bt.root = Node(4)
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 3)
        self.assertEqual(bt.root, node_to_add_to)

    def test_determine_node_to_add_to_root_only_larger_value(self):
        bt = BinaryTree()
        bt.root = Node(4)
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 5)
        self.assertEqual(bt.root, node_to_add_to)

    #     4
    #    /
    #   3
    def test_determine_node_to_add_to_smaller_value_one_left_child_exists(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(3)
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 2)
        self.assertEqual(bt.root.left_child, node_to_add_to)

    #     4
    #      \
    #       5
    def test_determine_node_to_add_to_larger_value_one_right_child_exists(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.right_child = Node(8)
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 5)
        self.assertEqual(bt.root.right_child, node_to_add_to)

    #        4
    #      /   \
    #     2     6
    #      \   / \
    #       3 4   8
    def test_determine_node_to_add_to_multiple_nodes_exist(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(4)
        bt.root.right_child.right_child = Node(8)
        # test 1
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 5)
        self.assertEqual(bt.root.right_child.left_child, node_to_add_to)
        # test 2
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 1)
        self.assertEqual(bt.root.left_child, node_to_add_to)
        # test 3
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 2)
        self.assertEqual(bt.root.left_child.right_child, node_to_add_to)
        # test 4
        node_to_add_to = bt._determine_node_to_add_to(bt.root, 9)
        self.assertEqual(bt.root.right_child.right_child, node_to_add_to)

    #        4
    #      /   \
    #     2     6
    #      \   / \
    #       3 5   8
    #            / \
    #           7   12
    def test_find_node(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(5)
        bt.root.right_child.right_child = Node(8)
        bt.root.right_child.right_child.left_child = Node(7)
        bt.root.right_child.right_child.right_child = Node(12)
        # test 1
        found_node, previous_node = bt.find_node(bt.root, None, 4)
        self.assertEqual(bt.root, found_node)
        self.assertEqual(None, previous_node)
        # test 2
        found_node, previous_node = bt.find_node(bt.root, None, 2)
        self.assertEqual(bt.root.left_child, found_node)
        self.assertEqual(bt.root, previous_node)
        # test 3
        found_node, previous_node = bt.find_node(bt.root, None, 12)
        self.assertEqual(bt.root.right_child.right_child.right_child, found_node)
        self.assertEqual(bt.root.right_child.right_child, previous_node)
        # test 4:
        found_node, previous_node = bt.find_node(bt.root, None, 999)
        self.assertEqual(None, found_node)
        self.assertEqual(None, previous_node)

    # CASE 1 - TEST 1
    # BEFORE:
    #        4
    #      /   \
    #     2     8
    #    / \   / \
    #   1   3 6   9
    #        /
    #       5
    def test_get_left_most_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(8)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(6)
        bt.root.right_child.right_child = Node(9)
        bt.root.right_child.left_child.left_child = Node(5)
        left_most_node, previous_left_most_node = bt._get_left_most_child(bt.root.right_child)
        self.assertEqual(5, left_most_node.value)
        self.assertEqual(6, previous_left_most_node.value)

    # CASE 1 - TEST 1
    # BEFORE:                   AFTER:
    #        4                      4
    #      /   \                  /   \
    #     2     8                2     8
    #    / \   / \              / \     \
    #   1   3 6   9            1   3     9
    def test_delete_node_remove_left_leaf_node(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(8)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(6)
        bt.root.right_child.right_child = Node(9)
        bt.count = 7
        bt.delete_node(6)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(8, bt.root.right_child.value)
        self.assertEqual(None, bt.root.right_child.left_child)
        self.assertEqual(9, bt.root.right_child.right_child.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(6, bt.count)

    # CASE 1 - TEST 2
    # BEFORE:                   AFTER:
    #        4                      4
    #      /   \                  /   \
    #     2     8                2     8
    #    / \   / \              / \   /
    #   1   3 6   9            1   3 6
    def test_delete_node_remove_right_leaf_node(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(8)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(6)
        bt.root.right_child.right_child = Node(9)
        bt.count = 7
        bt.delete_node(9)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(8, bt.root.right_child.value)
        self.assertEqual(6, bt.root.right_child.left_child.value)
        self.assertEqual(None, bt.root.right_child.right_child)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(6, bt.count)

    # CASE 2 - TEST 1
    # BEFORE:                   AFTER:
    #        4                      4
    #      /   \                  /   \
    #     2     8                2     6
    #    / \   /                / \   / \
    #   1   3 6                1   3 5   7
    #        / \
    #       5   7
    def test_delete_node_remove_node_with_left_child_but_no_right_child_right_side(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(8)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(6)
        bt.root.right_child.left_child.left_child = Node(5)
        bt.root.right_child.left_child.right_child = Node(7)
        bt.count = 8
        bt.delete_node(8)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(6, bt.root.right_child.value)
        self.assertEqual(5, bt.root.right_child.left_child.value)
        self.assertEqual(7, bt.root.right_child.right_child.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(7, bt.count)

    # CASE 2 - TEST 2
    # BEFORE:                   AFTER:
    #        14                    14
    #       /  \                  /  \
    #     10    20              10    20
    #    /  \                   / \
    #   9    12                7   12
    #  /
    # 7
    def test_delete_node_remove_node_with_left_child_but_no_right_child_left_side(self):
        bt = BinaryTree()
        bt.root = Node(14)
        bt.root.left_child = Node(10)
        bt.root.right_child = Node(20)
        bt.root.left_child.left_child = Node(9)
        bt.root.left_child.right_child = Node(12)
        bt.root.left_child.left_child.left_child = Node(7)
        bt.count = 6
        bt.delete_node(9)
        self.assertEqual(14, bt.root.value)
        self.assertEqual(10, bt.root.left_child.value)
        self.assertEqual(12, bt.root.left_child.right_child.value)
        self.assertEqual(7, bt.root.left_child.left_child.value)
        self.assertEqual(20, bt.root.right_child.value)
        self.assertEqual(5, bt.count)

    # CASE 3 - TEST 1
    # BEFORE:                   AFTER:
    #        4                      4
    #      /   \                  /   \
    #     2     6                2     7
    #    / \   / \              / \   / \
    #   1   3 5   7            1   3 5   8
    #              \
    #               8
    def test_delete_node_remove_node_with_right_child_that_has_no_left_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(5)
        bt.root.right_child.right_child = Node(7)
        bt.root.right_child.right_child.right_child = Node(8)
        bt.count = 8
        bt.delete_node(6)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(7, bt.root.right_child.value)
        self.assertEqual(5, bt.root.right_child.left_child.value)
        self.assertEqual(8, bt.root.right_child.right_child.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(7, bt.count)

    # CASE 4 - TEST 1
    # BEFORE:                   AFTER:
    #        4                      4
    #      /   \                  /   \
    #     2     6                2     7
    #    / \   / \              / \   / \
    #   1   3 5   8            1   3 5   8
    #            /
    #           7
    def test_delete_node_remove_node_with_right_child_that_has_a_left_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(5)
        bt.root.right_child.right_child = Node(8)
        bt.root.right_child.right_child.left_child = Node(7)
        bt.count = 8
        bt.delete_node(6)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(7, bt.root.right_child.value)
        self.assertEqual(5, bt.root.right_child.left_child.value)
        self.assertEqual(8, bt.root.right_child.right_child.value)
        self.assertEqual(None, bt.root.right_child.right_child.left_child)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(7, bt.count)

    # CASE 4 - TEST 2
    # BEFORE:                   AFTER:
    #        4                      4
    #      /   \                  /   \
    #     2    15                2    17
    #    / \   / \              / \   / \
    #   1   3 5  25            1   3 5  25
    #            /                      /
    #           19                     19
    #          /  \                   /  \
    #         18   20                18   20
    #         /
    #        17
    def test_delete_node_remove_node_with_right_child_that_has_a_left_child_and_left_grandchildren(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(15)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(5)
        bt.root.right_child.right_child = Node(25)
        bt.root.right_child.right_child.left_child = Node(19)
        bt.root.right_child.right_child.left_child.right_child = Node(20)
        bt.root.right_child.right_child.left_child.left_child = Node(18)
        bt.root.right_child.right_child.left_child.left_child.left_child = Node(17)
        bt.count = 11
        bt.delete_node(15)
        self.assertEqual(4, bt.root.value)
        self.assertEqual(17, bt.root.right_child.value)
        self.assertEqual(5, bt.root.right_child.left_child.value)
        self.assertEqual(25, bt.root.right_child.right_child.value)
        self.assertEqual(19, bt.root.right_child.right_child.left_child.value)
        self.assertEqual(18, bt.root.right_child.right_child.left_child.left_child.value)
        self.assertEqual(20, bt.root.right_child.right_child.left_child.right_child.value)
        self.assertEqual(None, bt.root.right_child.right_child.left_child.left_child.left_child)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(1, bt.root.left_child.left_child.value)
        self.assertEqual(3, bt.root.left_child.right_child.value)
        self.assertEqual(10, bt.count)

    # BEFORE:                   AFTER:
    #        4                     6
    #      /   \                  / \
    #     2     6                2   8
    #            \
    #             8
    def test_delete_node_remove_root_right_and_left_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.right_child.right_child = Node(8)
        bt.count = 4
        bt.delete_node(4)
        self.assertEqual(6, bt.root.value)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(8, bt.root.right_child.value)
        self.assertEqual(None, bt.root.right_child.right_child)
        self.assertEqual(3, bt.count)

    # BEFORE:                   AFTER:
    #        4                     6
    #          \
    #           6
    def test_delete_node_remove_root_only_right_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.right_child = Node(6)
        bt.count = 2
        bt.delete_node(4)
        self.assertEqual(6, bt.root.value)
        self.assertEqual(None, bt.root.left_child)
        self.assertEqual(None, bt.root.right_child)
        self.assertEqual(1, bt.count)

    # BEFORE:                   AFTER:
    #        4                    2
    #      /                     /
    #     2                     1
    #    /
    #   1
    def test_delete_node_remove_root_only_left_child(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.left_child.left_child = Node(1)
        bt.count = 3
        bt.delete_node(4)
        self.assertEqual(2, bt.root.value)
        self.assertEqual(1, bt.root.left_child.value)
        self.assertEqual(None, bt.root.right_child)
        self.assertEqual(None, bt.root.left_child.left_child)
        self.assertEqual(2, bt.count)

    # BEFORE:                   AFTER:
    #        4                      5
    #      /   \                  /   \
    #     2     6                2     6
    #    / \   / \              / \     \
    #   1   3 5   8            1   3     8
    #            /                      /
    #           7                      7
    def test_delete_node_remove_root_right_and_left_child_with_grandchildren(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(5)
        bt.root.right_child.right_child = Node(8)
        bt.root.right_child.right_child.left_child = Node(7)
        bt.count = 8
        bt.delete_node(4)
        self.assertEqual(5, bt.root.value)
        self.assertEqual(6, bt.root.right_child.value)
        self.assertEqual(None, bt.root.right_child.left_child)
        self.assertEqual(2, bt.root.left_child.value)
        self.assertEqual(8, bt.root.right_child.right_child.value)
        self.assertEqual(7, bt.root.right_child.right_child.left_child.value)
        self.assertEqual(7, bt.count)

    #        4
    #      /   \
    #     2     6
    #    / \   / \
    #   1   3 5   7
    @unittest.skip("not fully implemented yet")
    def test_enumerate_pre_order(self):
        bt = BinaryTree()
        bt.root = Node(4)
        bt.root.left_child = Node(2)
        bt.root.right_child = Node(6)
        bt.root.left_child.left_child = Node(1)
        bt.root.left_child.right_child = Node(3)
        bt.root.right_child.left_child = Node(5)
        bt.root.right_child.right_child = Node(7)
        node_values = bt.enumerate_pre_order(bt.root)
        self.assertEqual([4,2,1,3,6,5,7], node_values)

if __name__ == '__main__':
    unittest.main()
