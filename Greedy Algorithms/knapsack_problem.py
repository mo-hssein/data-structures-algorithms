import unittest


def knapsack_greedy(values, weights, size):
    """
    Solve the knapsack problem using a greedy approach.
    time complexty = O(n log n)

    Parameters:
    - values (list): A list of values for each item.
    - weights (list): A list of weights for each item.
    - size (int): The maximum capacity of the knapsack.

    Returns:
    - items, bag_values (tuple), (int): A tuple containing a list of selected items and the total value.
    """
    n = len(values)
    value_per_weight = [
        (values[i] / weights[i], values[i], weights[i]) for i in range(n)
    ]  
    value_per_weight.sort(reverse=True)  
    bag_values = 0
    bag_weights = 0
    items = []

    for element, values, weights in value_per_weight:  
        if (bag_weights + weights) <= size:
            bag_values += values
            bag_weights += weights
            items.append((element, weights))

    return items, bag_values


# unit testing

#      |
#      |
#      V


class TestGreedy(unittest.TestCase):
    def test_knapsack_greedy(self):
        values = [10, 5, 15, 7, 6, 18]
        weights = [2, 3, 5, 7, 1, 4]
        size = 15
        expected_items = [
            (6.0, 1),
            (5.0, 2),
            (4.5, 4),
            (3.0, 5),
            (1.6666666666666667, 3),
        ]
        items, _ = knapsack_greedy(values, weights, size)
        self.assertEqual(items, expected_items)


if __name__ == "__main__":
    unittest.main()
