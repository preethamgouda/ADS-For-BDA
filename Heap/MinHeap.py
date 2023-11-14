class CustomMinHeap:
    def __init__(self, values=[]):
        """
        Initialize the min heap with optional initial values.
        """
        self.heap_data = values
        self._build_heap()

    def is_heap_empty(self):
        """
        Check if the heap is empty.
        """
        return len(self.heap_data) == 0

    def get_heap_count(self):
        """
        Get the count of elements in the heap.
        """
        return len(self.heap_data)

    def _parent_index(self, idx):
        """
        Get the index of the parent element.
        """
        return (idx - 1) // 2

    def _left_child_index(self, idx):
        """
        Get the index of the left child element.
        """
        return 2 * idx + 1

    def _right_child_index(self, idx):
        """
        Get the index of the right child element.
        """
        return 2 * idx + 2

    def _swap_elements(self, i, j):
        """
        Swap elements at indices i and j in the heap.
        """
        self.heap_data[i], self.heap_data[j] = self.heap_data[j], self.heap_data[i]

    def _build_heap(self):
        """
        Build the heap from the initial values.
        """
        length = len(self.heap_data)
        start = (length - 2) // 2
        for idx in range(start, -1, -1):
            self._down_heap(idx, length)

    def _down_heap(self, idx, length):
        """
        Perform down-heap operation starting from index idx.
        """
        if self._left_child_index(idx) < length:
            left = self._left_child_index(idx)
            small_child = left
            if self._right_child_index(idx) < length:
                right = self._right_child_index(idx)
                if self.heap_data[right] < self.heap_data[left]:
                    small_child = right
            if self.heap_data[small_child] < self.heap_data[idx]:
                self._swap_elements(small_child, idx)
                self._down_heap(small_child, length)

    def add_heap_element(self, key):
        """
        Add a new element to the heap.
        """
        self.heap_data.append(key)
        self._up_heap(len(self.heap_data) - 1)

    def _up_heap(self, j):
        """
        Perform up-heap operation starting from index j.
        """
        parent = self._parent_index(j)
        if j > 0 and self.heap_data[j] < self.heap_data[parent]:
            self._swap_elements(j, parent)
            self._up_heap(parent)

    def get_min_heap_element(self):
        """
        Get the minimum element in the heap.
        """
        return self.heap_data[0]

    def delete_heap_min(self):
        """
        Delete the minimum element from the heap.
        """
        self._swap_elements(0, len(self.heap_data) - 1)
        element = self.heap_data.pop()
        self._down_heap(0, len(self.heap_data) - 1)
        return element

    def test_min_heap(self):
        """
        Test if the heap satisfies the min heap property.
        """
        if not self.is_heap_empty():
            for idx in range(len(self.heap_data) - 1, 0, -1):
                assert self.heap_data[idx] >= self.heap_data[self._parent_index(idx)]

    def heap_sort(self):
        """
        Perform heap sort on the heap.
        """
        if not self.is_heap_empty():
            for i in range(len(self.heap_data) - 1, 0, -1):
                self._swap_elements(0, i)
                self._down_heap(0, i)
            return self.heap_data


# Example usage and assertions
custom_min_heap = CustomMinHeap()
custom_min_heap.add_heap_element(50)
custom_min_heap.add_heap_element(10)
custom_min_heap.add_heap_element(15)
custom_min_heap.add_heap_element(60)
custom_min_heap.add_heap_element(90)
custom_min_heap.add_heap_element(5)
custom_min_heap.add_heap_element(75)
custom_min_heap.test_min_heap()
assert custom_min_heap.get_heap_count() == 7
assert custom_min_heap.get_min_heap_element() == 5
assert custom_min_heap.delete_heap_min() == 5
assert custom_min_heap.get_min_heap_element() == 10
assert custom_min_heap.delete_heap_min() == 10
assert custom_min_heap.get_min_heap_element() == 15
assert custom_min_heap.heap_sort() == [90, 75, 60, 50, 15]
