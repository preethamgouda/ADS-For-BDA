class CustomMaxHeap:
    def __init__(self, values=[]):
        self.heap_data = values
        self._build_custom_heap()

    def is_heap_empty(self):
        return len(self.heap_data) == 0

    def get_heap_count(self):
        return len(self.heap_data)

    def _parent_index(self, idx):
        return (idx - 1) // 2

    def _left_child_index(self, idx):
        return 2 * idx + 1

    def _right_child_index(self, idx):
        return 2 * idx + 2

    def _swap_elements(self, i, j):
        self.heap_data[i], self.heap_data[j] = self.heap_data[j], self.heap_data[i]

    def _build_custom_heap(self):
        length = len(self.heap_data)
        start = (length - 2) // 2
        for idx in range(start, -1, -1):
            self._down_heap_custom(idx, length)

    def _down_heap_custom(self, idx, length):
        if self._left_child_index(idx) < length:
            left = self._left_child_index(idx)
            big_child = left
            if self._right_child_index(idx) < length:
                right = self._right_child_index(idx)
                if self.heap_data[right] > self.heap_data[left]:
                    big_child = right
            if self.heap_data[big_child] > self.heap_data[idx]:
                self._swap_elements(big_child, idx)
                self._down_heap_custom(big_child, length)

    def add_heap_element(self, key):
        self.heap_data.append(key)
        self._up_heap_custom(len(self.heap_data) - 1)

    def _up_heap_custom(self, j):
        parent = self._parent_index(j)
        if j > 0 and self.heap_data[j] > self.heap_data[parent]:
            self._swap_elements(j, parent)
            self._up_heap_custom(parent)

    def get_max_heap_element(self):
        return self.heap_data[0]

    def delete_heap_max(self):
        self._swap_elements(0, len(self.heap_data) - 1)
        element = self.heap_data.pop()
        self._down_heap_custom(0, len(self.heap_data) - 1)
        return element

    def test_custom_max_heap(self):
        if not self.is_heap_empty():
            for idx in range(len(self.heap_data) - 1, 0, -1):
                assert self.heap_data[idx] <= self.heap_data[self._parent_index(idx)]

    def custom_heap_sort(self):
        if not self.is_heap_empty():
            for i in range(len(self.heap_data) - 1, 0, -1):
                self._swap_elements(0, i)
                self._down_heap_custom(0, i)
            return self.heap_data


custom_heap = CustomMaxHeap()
custom_heap.add_heap_element(100)
custom_heap.add_heap_element(30)
custom_heap.add_heap_element(50)
custom_heap.add_heap_element(120)
custom_heap.add_heap_element(180)
custom_heap.add_heap_element(10)
custom_heap.add_heap_element(150)
custom_heap.test_custom_max_heap()
assert custom_heap.get_heap_count() == 7
assert custom_heap.get_max_heap_element() == 180
assert custom_heap.delete_heap_max() == 180
assert custom_heap.get_max_heap_element() == 150
assert custom_heap.delete_heap_max() == 150
assert custom_heap.get_max_heap_element() == 120
assert custom_heap.custom_heap_sort() == [10, 30, 50, 100, 120]
