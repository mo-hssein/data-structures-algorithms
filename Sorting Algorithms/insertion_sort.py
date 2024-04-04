import unittest

def insertion_sort(arr):
    """
    Insertion sorting algorithm.
    Time complexty = O(n^2)

    Parameter:
    - arr (list): Unsorted array
    """
    n = len(arr)
    for i in range(1, n):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# unit testing

#      |
#      |
#      V

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [11, 6, 1, 9, 15, 100, 2, 13, 5, 55, 20, 35, 3, 7]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 6, 7, 9, 11, 13, 15, 20, 35, 55, 100])


if __name__ == "__main__":
    unittest.main()
