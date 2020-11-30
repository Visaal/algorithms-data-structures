"""
BINARY TREES (binary search tree)
Data structure that stores items in a tree rather than a chain
Chain nodes in a hierarchical manner rather than a linear one
Node at top is known as the root or head node
Leaf nodes or Terminal nodes are those that have no nodes under them
Child nodes have nodes under them

            HEAD
              |
        --------------
        |     |      |
      Child   Leaf   Child
        |             |
      -----         ------
      |    |        |     |
    Leaf  Leaf     Leaf  Leaf

There is only one path from the root to any leaf and in turn only one root up from any leaf to the root
This limitation is never violated

Binary Trees have 0 to 2 children and those children can only have 0 to 2 children and so on
There is a left child and right child if a node has two children
If a child has children then it is itself a tree

Binary Search Trees have additional data rule for child nodes where smaller values are on the left and larger on the right
Equal values are treated as larger values

Efficient for searching - do not have to potentially look at every node to find a value
Adding nodes is easy
Removing nodes is difficult

Add
Use a recursive algorithm
If adding a node to an empty tree it automatically becomes the root
If adding a second node if it is smaller then it is added to the left
If adding a third node if it is smaller than the second node then it will be added to the left of the second node
If adding a larger node it is added to the right
Equal values are treated as larger values

     4
    / \
   2   6
  /   / \
 1   4   7

Remove
Search
Traverse (Pre-Order, In-Order, Post-Order)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = 0

    # add node recursively
    def add_node(self, value):
        if self.count == 0:
            self.root = Node(value)
        else:
            node_to_add_to = self._determine_node_to_add_to(self.root, value)
            self._add_node_to_parent(node_to_add_to, value)
        self.count += 1

    def _determine_node_to_add_to(self, node, value):
        child_node = self._left_or_right_child(node, value)
        if child_node:
            return self._determine_node_to_add_to(child_node, value)
        else:
            return node

    def _left_or_right_child(self, node, new_value):
        if new_value < node.value:
            return node.left_child
        else:
            return node.right_child

    def _add_node_to_parent(self, parent_node, value):
        if value < parent_node.value:
            parent_node.left_child = Node(value)
        else:
            parent_node.right_child = Node(value)

    def find_node(self, node, previous_node, value):
        current_node = node
        if current_node is None:
            return None, None
        elif current_node.value == value:
            return current_node, previous_node
        else:
            previous_node = current_node
            current_node = self._left_or_right_child(current_node, value)
            return self.find_node(current_node, previous_node, value)

    def _get_left_most_child(self, node):
        previous_node = None
        left_most_node = node
        while left_most_node.left_child:
            previous_node = left_most_node
            left_most_node = left_most_node.left_child
        return left_most_node, previous_node

    def delete_node(self, value):
        node_to_delete, previous_node = self.find_node(self.root, None, value)
        # CASE 1: LEAF NODE
        # BEFORE:                   AFTER:
        #        4                      4
        #      /   \                  /   \
        #     2     8                2     8
        #    / \   / \              / \     \
        #   1   3 6   9            1   3     9
        if not node_to_delete.left_child and not node_to_delete.right_child:
            # check whether node to delete is a left or right child and remove pointer to it
            if node_to_delete.value < previous_node.value:
                previous_node.left_child = None
            else:
                previous_node.right_child = None

        # CASE 2: NODE TO DELETE HAS LEFT CHILD AND NO RIGHT CHILD
        # e.g.
        # BEFORE:                   AFTER:
        #        4                      4
        #      /   \                  /   \
        #     2     8                2     6
        #    / \   /                / \   / \
        #   1   3 6                1   3 5   7
        #        / \
        #       5   7
        elif node_to_delete.left_child and not node_to_delete.right_child:
            # Promote left child
            if not previous_node:
                self.root = None
                self.root = node_to_delete.left_child
            else:
                if node_to_delete.value < previous_node.value:
                    previous_node.left_child = node_to_delete.left_child
                else:
                    previous_node.right_child = node_to_delete.left_child

        # CASE 3: NODE TO DELETE HAS RIGHT CHILD AND THAT RIGHT CHILD HAS NO LEFT CHILD
        # e.g.
        # BEFORE:                   AFTER:
        #        4                      4
        #      /   \                  /   \
        #     2     6                2     7
        #    / \   / \              / \   / \
        #   1   3 5   7            1   3 5   8
        #              \
        #               8
        elif node_to_delete.right_child and not node_to_delete.right_child.left_child:
            #  Promote right child and change pointer to node to delete left child
            if not previous_node:
                node_to_delete.right_child.left_child = node_to_delete.left_child
                self.root = None
                self.root = node_to_delete.right_child
            else:
                node_to_delete.right_child.left_child = node_to_delete.left_child
                previous_node.right_child = node_to_delete.right_child

        # CASE 4: NODE TO DELETE HAS RIGHT CHILD AND THAT RIGHT CHILD HAS A LEFT CHILD
        # e.g.
        # BEFORE:                   AFTER:
        #        4                      4
        #      /   \                  /   \
        #     2     6                2     7
        #    / \   / \              / \   / \
        #   1   3 5   8            1   3 5   8
        #            /
        #           7
        #
        # e.g. 2
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
        elif node_to_delete.right_child and node_to_delete.right_child.left_child:
            # Need to promote the left most child under node_to_delete.right_child
            left_most_child, previous_most_left_node = self._get_left_most_child(node_to_delete.right_child)
            if not previous_node:
                left_most_child.left_child = node_to_delete.left_child
                left_most_child.right_child = node_to_delete.right_child
                previous_most_left_node.left_child = None
                self.root = None
                self.root = left_most_child
            else:
                previous_node.right_child = left_most_child
                left_most_child.left_child = node_to_delete.left_child
                left_most_child.right_child = node_to_delete.right_child
                previous_most_left_node.left_child = None

        self.count -= 1

    def enumerate_pre_order(self, node):
        if node:
            print(node.value)
            self.enumerate_pre_order(node.left_child)
            self.enumerate_pre_order(node.right_child)
