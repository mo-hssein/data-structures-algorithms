import unittest


def swap(arr, item_one, item_two):
    """
    This function swaps two values in a list.
    time complexty = O(1)


    Args:
    - arr (list): The list containing the elements to be swapped.
    - item_one (int): The index of the first item to be swapped.
    - item_two (int): The index of the second item to be swapped.
    """
    arr[item_one], arr[item_two] = arr[item_two], arr[item_one]


def partition(arr, low, high):
    """
    This function partitions the list around the pivot element.
    time complexty = O(n)

    Args:
    - arr (list): The list to be partitioned.
    - low (int): The index for the lower bound.
    - high (int): The index for the upper bound.

    Returns:
    - The index of the pivot element after partitioning.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1


def quick_sort(arr, low, high):
    """
    Sorts a list of integers using the quicksort algorithm.
    time complexty = O(n log n)

    Args:
    - arr (list): The list to be sorted.
    - low (int): The index of the first element in the sublist.
    - high (int): The index of the last element in the sublist.

    Returns:
    - arr (list): The sorted list.
    """
    if len(arr) < 2:
        return arr

    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr


# unit testing

#      |
#      |
#      V


class TestQuickSort(unittest.TestCase):
    def test_partition(self):
        arr = [1, 8, 10, 13, 5, 2, 7, 4]
        self.assertEqual(partition(arr, 0, (len(arr) - 1)), 2)

    def test_quick_sort(self):

        # test array have more than 2 element
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(
            quick_sort(arr, 0, (len(arr) - 1)), [1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

        # test array have less than 2 element
        arr = [8]
        self.assertEqual(quick_sort(arr, 0, (len(arr) - 1)), [8])

        # test empty array
        arr = []
        self.assertEqual(quick_sort(arr, 0, (len(arr) - 1)), [])

if __name__ == "__main__":
    unittest.main()
