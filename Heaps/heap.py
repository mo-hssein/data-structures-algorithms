from abc import ABC, abstractmethod
import unittest


class Inter_face_For_Max_Heap(ABC):
    """
    The interface for max heap implementation
    """

    @abstractmethod
    def what_is_parent_for_element(self, value):
        pass

    @abstractmethod
    def left_child_for_element(self, value):
        pass

    @abstractmethod
    def right_child_for_element(self, value):
        pass

    @abstractmethod
    def swap(self, i, j):
        pass

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def shift_up(self, index):
        pass

    @abstractmethod
    def shift_down(self, index):
        pass

    @abstractmethod
    def sort(self):
        pass


class Max_Heap(Inter_face_For_Max_Heap):
    """The implementation for max heap"""

    def __init__(self) -> None:
        super().__init__()
        self.size = 0
        self.heap = []

    def what_is_parent_for_element(self, value):
        """
        Calculates the index of the parent element for a given element index
        """
        if value == 0:
            return 0
        return (value - 1) // 2

    def left_child_for_element(self, value):
        """
        Calculates the index of the left child for a given element index
        """
        left_child_index = 2 * value + 1
        if left_child_index < self.size:
            return left_child_index
        return None

    def right_child_for_element(self, value):
        """
        Calculates the index of the right child for a given element index
        """
        right_child_index = 2 * value + 2
        if right_child_index < self.size:
            return right_child_index
        return None

    def swap(self, i, j):
        """
        Swaps the elements at the given indices in the heap
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, vaule):
        """
        Inserts a value into the max heap
        time complexty = O(log n)
        """

        self.heap.append(vaule)
        index = len(self.heap) - 1
        self.shift_up(index)
        self.size += 1

    def shift_up(self, index):
        """
        Moves the element up the heap to maintain the max heap property
        """
        while index > 0:
            parent = self.what_is_parent_for_element(index)
            if parent >= 0:
                if self.heap[index] > self.heap[parent]:
                    self.swap(index, parent)
                else:
                    break
                index = parent
            else:
                break

    def delete(self, value):
        """
        Deletes the specified value from the max heap
        time complexty = O(log n)
        """
        index = self.heap.index(value)
        if value not in self.heap:
            return False
        else:
            last_index = len(self.heap) - 1
            self.heap[index] = self.heap[last_index]
            self.heap.pop(last_index)
            self.size -= 1
            self.shift_down(index)
            return True

    def shift_down(self, index):
        """
        Moves the element down the heap to maintain the max heap property
        """
        while index < len(self.heap):
            left = self.left_child_for_element(index)
            right = self.right_child_for_element(index)
            if left is not None and right is not None:
                if right < len(self.heap) and left < len(self.heap):
                    if self.heap[left] > self.heap[right]:
                        if self.heap[left] > self.heap[index]:
                            self.swap(left, index)
                            index = left
                        else:
                            break
                    elif self.heap[right] > self.heap[left]:
                        if self.heap[right] > self.heap[index]:
                            self.swap(right, index)
                            index = right
                        else:
                            break
                    else:
                        break
            elif left is not None and right is None:
                if left < len(self.heap):
                    if self.heap[left] > self.heap[index]:
                        self.swap(left, index)
                        index = left
                    else:
                        break
            elif right is not None and left is None:
                if right < len(self.heap):
                    if self.heap[right] > self.heap[index]:
                        self.swap(left, index)
                        index = right
                    else:
                        break
            else:
                break

    def sort(self):
        """
        Sorts the max heap
        time complexty = O(n log n)
        """
        sorted_arry = []
        while len(self.heap) > 0:
            root = self.heap[0]
            sorted_arry.insert(0, root)
            self.delete(root)
        return sorted_arry


# unit testing

#      |
#      |
#      V


class TestMaxHeap(unittest.TestCase):
    def test_insert(self):
        """
        Test insertion and sorting
        """
        max_heap = Max_Heap()
        array = [5, 3, 8, 1, 9, 6, 7]
        for value in array:
            max_heap.insert(value)
        sorted_array = max_heap.sort()
        self.assertEqual(sorted_array, [1, 3, 5, 6, 7, 8, 9])

    def test_delete(self):
        """
        Test deletion
        """
        max_heap = Max_Heap()
        array = [5, 3, 8, 1, 9, 6, 7]
        for value in array:
            max_heap.insert(value)

        max_heap.delete(9)
        self.assertEqual(max_heap.heap, [8, 6, 7, 1, 3, 5])

        max_heap.delete(1)
        self.assertEqual(max_heap.heap, [8, 6, 7, 5, 3])

        max_heap.delete(5)
        self.assertEqual(max_heap.heap, [8, 6, 7, 3])

        max_heap.delete(6)
        self.assertEqual(max_heap.heap, [8, 3, 7])

    def test_sort(self):
        """
        Test sorting
        """
        max_heap = Max_Heap()
        array = [5, 3, 8, 1, 9, 6, 7]
        for value in array:
            max_heap.insert(value)

        sorted_array = max_heap.sort()
        self.assertEqual(sorted_array, [1, 3, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
