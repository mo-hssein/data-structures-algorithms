import unittest


def swap(arr, item_one, item_two):
    """
    This function swaps two values in a list.

    Args:
    - arr (list): The list containing the elements to be swapped.
    - item_one (int): The index of the first item to be swapped.
    - item_two (int): The index of the second item to be swapped.
    """
    arr[item_two], arr[item_one] = arr[item_one], arr[item_two]


def partition(arr):
    """
    This function partitions the list around the pivot element.
    time complexty = O(n)
    Args:
    - arr (list): The list to be partitioned.

    Returns:
    - The index of the pivot element after partitioning.
    """
    if len(arr) < 2:
        return 

    pivot = arr[-1]
    j = 0
    i = j - 1
    for j in range(len(arr)):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    return arr[i]


# unit testing

#      |
#      |
#      V

class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        arr = [1, 8, 10, 13, 5, 2, 7, 4]
        self.assertEqual(partition(arr), 4)

        arr = []
        self.assertEqual(partition(arr), None)

        arr = [5]
        self.assertEqual(partition(arr), None)
        
if __name__ == "__main__":
    unittest.main()
