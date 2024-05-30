import heapq
import unittest

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths from the start node to all other nodes in a weighted graph.

    Args:
    - graph (dict): A dictionary representing the weighted graph where the keys are node identifiers and the values are dictionaries of neighboring nodes and their respective edge weights.
    - start (str): The starting node identifier.

    Returns:
    - vertices (dict): A dictionary where the keys are node identifiers and the values are the shortest distances from the start node to each node.
    - parent (dict): A dictionary where the keys are node identifiers and the values are the parent nodes for each node in the shortest path tree.
    """

    # Initialize all vertices with an infinite value
    vertices = {} 
    for v in graph:
        vertices[v] = float("inf")

    # Initialize all vertices with an unknown parent
    parent = {}
    for v in graph:
        parent[v] = None

    # Initialize the starting vertex with a value of 0
    vertices[start] = 0

    # Initializing a queue structure of type heap, add the first vertex to it
    priority_queue = [(0, start)]

    # As long as the queue has items continue in the loop
    while priority_queue:
        # Drag the first item in the queue to act on its neighbors
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current distance is greater than the previously saved distance, skip this vertex
        if current_distance > vertices[current_vertex]:
            continue

        # If the current distance is smaller than the previously saved distance, we update the distances to take a smaller distance
        for neighbor, length in graph[current_vertex].items():
            distance = current_distance + length

            # If we find a shorter distance, we update it
            if distance < vertices[neighbor]:
                vertices[neighbor] = distance
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return vertices, parent


def shortest_path(parent, end):
    """
    Computes the shortest path from the start node to the end node using the parent dictionary resulting from Dijkstra's algorithm.

    Parameters:
    - parent (dict): A dictionary that specifies the parent of each node in the shortest path.
    - end (str): The ending node.

    Returns:
    - path (list): A list of nodes representing the shortest path from the start to the end.
    """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()  # Reverse the path to get it from start to end
    return path


# unit testing

#      |
#      |
#      V


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": {"B": 1, "C": 2, "D": 5},
            "B": {"A": 1, "D": 2, "E": 8},
            "C": {"A": 2, "D": 3, "F": 8, "H": 3},
            "D": {"A": 5, "B": 2, "C": 3, "E": 1, "F": 2, "G": 2},
            "E": {"B": 8, "D": 1, "K": 4},
            "F": {"C": 8, "D": 2, "G": 3, "H": 2, "I": 3},
            "G": {"D": 2, "F": 3, "I": 5, "J": 4, "K": 5},
            "H": {"C": 3, "F": 2, "I": 7},
            "I": {"F": 3, "G": 5, "J": 2, "H": 7},
            "J": {"G": 4, "I": 2, "K": 3},
            "K": {"E": 4, "G": 5, "J": 3},
        }

    def test_dijkstra(self):
        start = "A"
        expected_distances = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 5,
            "H": 5,
            "I": 8,
            "J": 9,
            "K": 8,
        }
        distances, parent = dijkstra(self.graph, start)
        self.assertEqual(distances, expected_distances)

    def test_shortest_path(self):
        start = "A"
        target = "J"
        _, parent = dijkstra(self.graph, start)
        expected_path = ["A", "B", "D", "G", "J"]
        path = shortest_path(parent, target)
        self.assertEqual(path, expected_path)


if __name__ == "__main__":
    unittest.main()
