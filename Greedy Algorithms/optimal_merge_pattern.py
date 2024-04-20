import unittest


def optimal_merge_pattern(sizes):
    """
    Merge the files optimally to minimize the total cost of merging.
    Time complexity: O(n log n)

    Args:
    - sizes (list[int]): List of files sizes.

    Returns:
    - cost (int): Total cost of merging.
    """

    # if sizes is small
    if len(sizes) < 1:
        return 0
    elif len(sizes) < 2:
        return sizes[0]

    # Sort the items in ascending order so we can combine them at the lowest cost
    sizes.sort()

    # final cost
    cost = 0

    # Loop to repeat the merge until only one element remains
    while len(sizes) > 1:
        first_digit = sizes.pop(0)
        second_digit = sizes.pop(0)
        cost += first_digit + second_digit
        sizes.append(first_digit + second_digit)

        # Sorting again to keep the lowest cost on top
        sizes.sort()

    return cost


class TestOptimalMergePattern(unittest.TestCase):
    def test_small_sizes(self):
        sizes = [10, 20, 30]
        expected_cost = 90
        self.assertEqual(optimal_merge_pattern(sizes), expected_cost)

    def test_large_sizes(self):
        sizes = [100, 200, 300, 400]
        expected_cost = 1900
        self.assertEqual(optimal_merge_pattern(sizes), expected_cost)

    def test_single_file(self):
        sizes = [50]
        expected_cost = 50
        self.assertEqual(optimal_merge_pattern(sizes), expected_cost)

    def test_empty_file(self):
        sizes = []
        expected_cost = 0
        self.assertEqual(optimal_merge_pattern(sizes), expected_cost)


if __name__ == "__main__":
    unittest.main()
