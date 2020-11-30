from stacks import Stack
from queue import FifoQueue


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self, nodes=None, edges=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

        if edges is None:
            edges = []
        self.edges = edges

    def insert_node(self, new_value):
        new_node = Node(new_value)
        self.nodes.append(new_node)
        return new_node

    def insert_edge(self, value, node_from_value, node_to_value):
        node_from = None
        node_to = None

        # Check if node already exists for the value specified
        for node in self.nodes:
            if node.value == node_from_value:
                node_from = node
            if node.value == node_to_value:
                node_to = node

        # If a node with value specified does not already exist one needs to be added
        if node_from is None:
            node_from = self.insert_node(node_from_value)
        if node_to is None:
            node_to = self.insert_node(node_to_value)

        new_edge = Edge(value, node_from, node_to)
        self.edges.append(new_edge)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = []
        for edge in self.edges:
            edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""

        # Determine what max index will be
        max_index = None
        if self.nodes:
            max_index = max([node.value for node in self.nodes]) + 1

        adjacency_list = []
        # Create a blank list with the required number of elements
        if max_index:
            adjacency_list = [None] * max_index

        # Place relevant nodes in their respective index positions
        for edge in self.edges:
            if adjacency_list[edge.node_from.value]:
                adjacency_list[edge.node_from.value].append((edge.node_to.value, edge.value))
            else:
                adjacency_list[edge.node_from.value] = [(edge.node_to.value, edge.value)]

        return adjacency_list

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        matrix = []
        matrix_length = max([node.value for node in self.nodes]) + 1

        # create blank matrix
        for i in range(matrix_length):
            matrix.append([0] * matrix_length)

        # determine matrix values and add the edges
        for edge in self.edges:
            row = edge.node_from.value
            col = edge.node_to.value
            matrix[row][col] = edge.value

        return matrix

    def _return_new_edge(self, current_node, visited_nodes):
        for edge in current_node.edges:
            if edge.node_to not in visited_nodes:
                return edge
        return None

    def depth_first_search(self):
        visited_nodes = []
        # Use stack to keep track while traversing so can move back to previous nodes
        node_stack = Stack()

        # Set starting point as no root node
        current_node = self.edges[0].node_from
        visited_nodes.append(current_node)
        node_stack.push(current_node)

        while current_node:
            new_edge = self._return_new_edge(current_node, visited_nodes)
            if new_edge:
                current_node = new_edge.node_to
                visited_nodes.append(current_node)
                node_stack.push(current_node)
            else:
                # pop twice to get back to the previous node as current node is on top of the stack
                node_stack.pop()
                current_node = node_stack.pop()

        node_values = [node.value for node in visited_nodes]

        return node_values

    def breadth_first_search(self):
        visited_nodes = []
        # Use a queue to keep track of all the nodes you need to visit
        node_queue = FifoQueue()

        # Set starting point as no root node
        current_node = self.edges[0].node_from
        visited_nodes.append(current_node)

        while current_node:
            new_edge = self._return_new_edge(current_node, visited_nodes)
            if new_edge:
                visited_nodes.append(new_edge.node_to)
                node_queue.enqueue(new_edge.node_to)
            else:
                current_node = node_queue.dequeue()

        visited_node_values = [node.value for node in visited_nodes]

        return visited_node_values