import unittest
from graph import Node, Edge, Graph


class TestNode(unittest.TestCase):

    def test_node_create(self):
        value = 8
        graph_node = Node(value)
        self.assertEqual(8, graph_node.value)
        self.assertEqual([], graph_node.edges)


class TestEdge(unittest.TestCase):

    def test_edge_create(self):
        value, node_from, node_to = '4 miles', Node(2), Node(8)
        edge = Edge(value, node_from, node_to)
        self.assertEqual('4 miles', edge.value)
        self.assertEqual(node_from, edge.node_from)
        self.assertEqual(node_to, edge.node_to)


class TestGraph(unittest.TestCase):

    def test_graph_create(self):
        node_list = [Node(1), Node(2), Node(3)]
        edge_list = [Edge('2 miles', node_list[0], node_list[1]), Edge('6 miles', node_list[1], node_list[2])]
        graph = Graph(node_list, edge_list)
        self.assertEqual(node_list, graph.nodes)
        self.assertEqual(edge_list, graph.edges)

    def test_graph_insert_node(self):
        graph = Graph()
        graph.insert_node(8)
        self.assertEqual(8, graph.nodes[0].value)

    def test_graph_insert_two_nodes(self):
        graph = Graph()
        graph.insert_node(7)
        graph.insert_node(3)
        self.assertEqual(7, graph.nodes[0].value)
        self.assertEqual(3, graph.nodes[1].value)

    def test_insert_edge_two_existing_nodes(self):
        graph = Graph()
        graph.insert_node(3)
        graph.insert_node(9)
        edge_value, node_from_value, node_to_value = '4m', 3, 9
        graph.insert_edge(edge_value, node_from_value, node_to_value)
        self.assertEqual(edge_value, graph.edges[0].value)
        self.assertEqual(node_from_value, graph.edges[0].node_from.value)
        self.assertEqual(node_to_value, graph.edges[0].node_to.value)

    def test_insert_edge_no_node_to(self):
        graph = Graph()
        graph.insert_node(4)
        edge_value, node_from_value, node_to_value = '5m', 4, 9
        graph.insert_edge(edge_value, node_from_value, node_to_value)
        self.assertEqual(edge_value, graph.edges[0].value)
        self.assertEqual(node_from_value, graph.edges[0].node_from.value)
        self.assertEqual(node_to_value, graph.edges[0].node_to.value)

    def test_insert_edge_no_node_from(self):
        graph = Graph()
        graph.insert_node(9)
        edge_value, node_from_value, node_to_value = '5m', 4, 9
        graph.insert_edge(edge_value, node_from_value, node_to_value)
        self.assertEqual(edge_value, graph.edges[0].value)
        self.assertEqual(node_from_value, graph.edges[0].node_from.value)
        self.assertEqual(node_to_value, graph.edges[0].node_to.value)

    def test_insert_edge_node_edge_list_updated(self):
        graph = Graph()
        n1 = graph.insert_node(6)
        n2 = graph.insert_node(11)
        edge_value, node_from_value, node_to_value = '6m', 6, 11
        graph.insert_edge(edge_value, node_from_value, node_to_value)
        self.assertEqual(n1.edges, graph.edges)
        self.assertEqual(n2.edges, graph.edges)
        n3 = graph.insert_node(23)
        edge_value, node_from_value, node_to_value = '6m', 11, 23
        graph.insert_edge(edge_value, node_from_value, node_to_value)
        self.assertIn(n3.edges[0], graph.edges)

    def test_get_edge_list(self):
        graph = Graph()
        graph.insert_edge('7m', 6, 11)
        graph.insert_edge('3m', 11, 15)
        edge_list = graph.get_edge_list()
        self.assertEqual([('7m', 6, 11), ('3m', 11, 15)], edge_list)

    def test_get_adjacency_list(self):
        graph = Graph()
        graph.insert_edge('7m', 2, 3)
        graph.insert_edge('5m', 2, 4)
        graph.insert_edge('3m', 3, 5)
        adjacency_list = graph.get_adjacency_list()
        self.assertEqual([None, None, [(3, '7m'), (4, '5m')], [(5, '3m')], None, None], adjacency_list)

    def test_get_adjacency_list_udacity_example(self):
        graph = Graph()
        graph.insert_edge(100, 1, 2)
        graph.insert_edge(101, 1, 3)
        graph.insert_edge(102, 1, 4)
        graph.insert_edge(103, 3, 4)
        adjacency_list = graph.get_adjacency_list()
        self.assertEqual([None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None], adjacency_list)

    def test_get_adjacency_matrix(self):
        graph = Graph()
        graph.insert_edge(100, 1, 2)
        graph.insert_edge(101, 1, 3)
        graph.insert_edge(102, 1, 4)
        graph.insert_edge(103, 3, 4)
        matrix = graph.get_adjacency_matrix()
        self.assertEqual([
            [0, 0, 0, 0, 0],
            [0, 0, 100, 101, 102],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 103],
            [0, 0, 0, 0, 0]
        ], matrix)

    def test_depth_first_search(self):
        graph = Graph()
        graph.insert_edge(100, 'g', 'r')
        graph.insert_edge(101, 'g', 'a')
        graph.insert_edge(103, 'r', 'a')
        graph.insert_edge(102, 'g', 'h')
        graph.insert_edge(103, 'r', 'p')
        node_values = graph.depth_first_search()
        self.assertEqual(['g', 'r', 'a', 'p', 'h'], node_values)

    def test_breadth_first_search(self):
        graph = Graph()
        graph.insert_edge(100, 'g', 'r')
        graph.insert_edge(101, 'g', 'a')
        graph.insert_edge(103, 'r', 'a')
        graph.insert_edge(102, 'g', 'h')
        graph.insert_edge(103, 'r', 'p')
        node_values = graph.breadth_first_search()
        self.assertEqual(['g', 'r', 'a', 'h', 'p'], node_values)

if __name__ == '__main__':
    unittest.main()
