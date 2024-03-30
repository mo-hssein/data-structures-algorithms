from abc import ABC, abstractmethod


class InterfaceForMaxHeap(ABC):
    """The interface for max heap implementation"""

    @abstractmethod
    def what_is_parent_for_element(self, index):
        pass

    @abstractmethod
    def left_child_for_element(self, index):
        pass

    @abstractmethod
    def right_child_for_element(self, index):
        pass

    @abstractmethod
    def swap(self, i, j):
        pass

    @abstractmethod
    def insert(self, index):
        pass

    @abstractmethod
    def delete(self, index):
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
