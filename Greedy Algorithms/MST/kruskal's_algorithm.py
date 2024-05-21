import heapq
import unittest
from unionfind import unionfind


class Graph:
    """
    A class to represent a graph using an adjacency list and provide
    a method to find the Minimum Spanning Tree (MST) using Kruskal's algorithm.

    Attributes
    - edges (list): List to store all the edges of the graph.
    - vertices (list): List to store all the vertices of the graph.

    Methods
    - kruskal (function): Computes the MST of the graph using Kruskal's algorithm and prints the edges and total cost of the MST.
    """

    def __init__(self, graph_dict):
        """
        Constructs all the necessary attributes for the Graph object.

        Parameters
        - graph_dict (dict): A dictionary where keys are vertices and values are lists of tuples.
        """
        # All edges.
        self.edges = []

        # All vertices.
        self.vertices = list(graph_dict.keys())

        for vertex in graph_dict:
            for edge in graph_dict[vertex]:
                weight, adjacent_vertex, _ = edge
                self.edges.append((weight, vertex, adjacent_vertex))

    def kruskal(self):
        """
        Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of the graph. Prints the edges in the MST and the total cost.
        """
        MST = []  # List to store the edges of the Minimum Spanning Tree (MST).

        # Initialize Union-Find structure.
        uf = unionfind(len(self.vertices))

        # Convert edges list into a heap (priority queue).
        heapq.heapify(self.edges)

        num_edges_in_mst = 0  # Counter for edges added to the MST.

        # Process edges until we have enough edges for the MST.
        while num_edges_in_mst < len(self.vertices) - 1 and self.edges:
            weight, vertex_u, vertex_v = heapq.heappop(self.edges)
            root_u = self.vertices.index(vertex_u)
            root_v = self.vertices.index(vertex_v)

            # Check if adding this edge would form a cycle.
            if uf.find(root_u) != uf.find(root_v):
                num_edges_in_mst += 1
                MST.append((vertex_u, vertex_v, weight))
                uf.unite(root_u, root_v)

        # Calculate the total cost of the MST.
        cost = 0
        # print("Edges in the constructed MST:")
        for vertex_u, vertex_v, weight in MST:
            cost += weight
        #     print(f"{vertex_u} -- {vertex_v} == {weight}")
        # print(f"Cost = {cost}")
        return MST, cost



# unit testing

#      |
#      |
#      V


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        # Graph data for testing
        self.graph_data = {
            "A": [(3, "D", "A"), (3, "C", "A"), (2, "B", "A")],
            "B": [(2, "A", "B"), (4, "C", "B"), (3, "E", "B")],
            "C": [
                (3, "A", "C"),
                (5, "D", "C"),
                (6, "F", "C"),
                (1, "E", "C"),
                (4, "B", "C"),
            ],
            "D": [(3, "A", "D"), (5, "C", "D"), (7, "F", "D")],
            "E": [(8, "F", "E"), (1, "C", "E"), (3, "B", "E")],
            "F": [(9, "G", "F"), (8, "E", "F"), (6, "C", "F"), (7, "D", "F")],
            "G": [(9, "F", "G")],
        }

        # Create a Graph object for testing
        self.graph = Graph(self.graph_data)

    def test_graph_initialization(self):
        self.assertEqual(set(self.graph.vertices), {"A", "B", "C", "D", "E", "F", "G"})
        self.assertEqual(
            set(self.graph.edges),
            {
                (3, "A", "D"),
                (3, "A", "C"),
                (2, "A", "B"),
                (2, "B", "A"),
                (4, "B", "C"),
                (3, "B", "E"),
                (3, "C", "A"),
                (5, "C", "D"),
                (6, "C", "F"),
                (1, "C", "E"),
                (4, "C", "B"),
                (3, "D", "A"),
                (5, "D", "C"),
                (7, "D", "F"),
                (8, "E", "F"),
                (1, "E", "C"),
                (3, "E", "B"),
                (9, "F", "G"),
                (8, "F", "E"),
                (6, "F", "C"),
                (7, "F", "D"),
                (9, "G", "F"),
            },
        )

    def test_kruskal_mst(self):
        mst, cost = self.graph.kruskal()
        expected_mst = {
            ("A", "C", 3),
            ("A", "B", 2),
            ("C", "E", 1),
            ("A", "D", 3),
            ("C", "F", 6),
            ("F", "G", 9),
        }
        self.assertEqual(set(mst), expected_mst)
        self.assertEqual(cost, 24)


if __name__ == "__main__":
    unittest.main()
