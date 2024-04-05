import unittest


def merge(left_half, right_half):
    """
    This function merges two sorted halves of a list.

    Args:
    - left_half (list): The left half of the list.
    - right_half (list): The right half of the list.

    Returns:
    - list: The merged and sorted list.
    """
    merged_arr = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged_arr.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged_arr.append(right_half[j])
        j += 1

    return merged_arr


def merge_sort(arr):
    """
    This function sorts the list using merge sort algorithm.

    Args:
    - arr (list): The list to be sorted.

    Returns:
    - list: The sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


# unit testing

#      |
#      |
#      V

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        arr_unsorted = [5, 2, 8, 3, 1]
        self.assertEqual(merge_sort(arr_unsorted), [1, 2, 3, 5, 8])

        arr_single = [1]
        self.assertEqual(merge_sort(arr_single), [1])

        arr_empty = []
        self.assertEqual(merge_sort(arr_empty), [])

        arr_duplicate = [3, 2, 5, 2, 3]
        self.assertEqual(merge_sort(arr_duplicate), [2, 2, 3, 3, 5])

if __name__ == "__main__":
    unittest.main()
