import heapq
import unittest

def prims(G, start="A"):
    """
    Prim's algorithm for finding Minimum Spanning Tree (MST) of a weighted directed graph.
    time complexity = O(E log E)

    Parameters:
    - G (dict): Graph represented as a dictionary where keys are nodes and values are lists of tuples representing the weighted edges connected to the node.
    - start (str): Starting node for the algorithm. Default is "A".

    Returns:
    - MST (list): List of tuples representing the edges in the Minimum Spanning Tree.
    - total_cost (int): Total cost of the Minimum Spanning Tree.
    """

    # List of unvisited nodes
    unvisited = list(G.keys())

    # List of visited nodes
    visited = []

    # List to store edges in the Minimum Spanning Tree (MST)
    MST = []

    # Total cost of the MST
    total_cost = 0

    # Remove the starting node from unvisited and add it to visited
    unvisited.remove(start)
    visited.append(start)

    # Heapify the heap with edges connected to the starting node
    heap = G[start]
    heapq.heapify(heap)

    # Main loop: Repeat until all nodes are visited
    while unvisited:

        # Extract the minimum cost edge from the heap
        if heap:
            (cost, n2, n1) = heapq.heappop(heap)
            new_node = None
        else:
            return

        # If one node is in the tree and the other is not
        if n1 in unvisited and n2 in visited:
            new_node = n1
            MST.append((cost, n1, n2))

        elif n1 in visited and n2 in unvisited:
            new_node = n2
            MST.append((cost, n2, n1))

        # If a new node is added to the tree
        if new_node != None:
            # Remove the new node from unvisited and add it to visited
            unvisited.remove(new_node)
            visited.append(new_node)
            total_cost += cost

            # Add edges connected to the new node to the heap
            for node in G[new_node]:
                heapq.heappush(heap, node)

    return MST, total_cost


class TestPrims(unittest.TestCase):
    def test_with_provided_graph(self):
        graph = {
            "A": [(3, "D", "A"), (3, "C", "A"), (2, "B", "A")],
            "B": [(2, "A", "B"), (4, "C", "B"), (3, "E", "B")],
            "C": [(3, "A", "C"),(5, "D", "C"),(6, "F", "C"),(1, "E", "C"),(4, "B", "C"),],
            "D": [(3, "A", "D"), (5, "C", "D"), (7, "F", "D")],
            "E": [(8, "F", "E"), (1, "C", "E"), (3, "B", "E")],
            "F": [(9, "G", "F"), (8, "E", "F"), (6, "C", "F"), (7, "D", "F")],
            "G": [(9, "F", "G")],
        }
        expected_result = ([(2, 'B', 'A'), (3, 'C', 'A'), (1, 'E', 'C'), (3, 'D', 'A'), (6, 'F', 'C'), (9, 'G', 'F')], 24)
        self.assertEqual(prims(graph), expected_result)

    def test_with_small_graph(self):
        small_graph = {
            "A": [(1, "B", "A"), (2, "C", "A")],
            "B": [(1, "A", "B"), (3, "C", "B")],
            "C": [(2, "A", "C"), (3, "B", "C")],
        }
        expected_result = ([(1, "B", "A"), (2, "C", "A")],3)
        self.assertEqual(prims(small_graph), expected_result)

    def test_with_disconnected_graph(self):
        disconnected_graph = {
            "A": [(1, "B", "A"), (2, "C", "A")],
            "B": [(1, "A", "B"), (3, "C", "B")],
            "C": [(2, "A", "C"), (3, "B", "C")],
            "D": [],
        }
        expected_result = None
        self.assertEqual(prims(disconnected_graph), expected_result)

    def test_with_negative_weight_graph(self):
        negative_weight_graph = {
            "A": [(1, "B", "A"), (-2, "C", "A")],
            "B": [(1, "A", "B"), (3, "C", "B")],
            "C": [(-2, "A", "C"), (3, "B", "C")],
        }
        expected_result = ([(-2, "C", "A"), (1, "B", "A")], -1)
        self.assertEqual(prims(negative_weight_graph), expected_result)


if __name__ == "__main__":
    unittest.main()
