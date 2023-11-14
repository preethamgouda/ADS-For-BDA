class singlyLinkedList:
    class Node:
        def __init__(self, value):
            self.data = value
            self.next = None

    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def add_to_start(self, value):
        new_node = self.Node(value)
        if not self.is_empty():
            new_node.next = self.start
            self.start = new_node
        else:
            self.start = self.end = new_node
        self.size += 1
        return self.start.data, self.end.data

    def add_to_end(self, value):
        new_node = self.Node(value)
        if not self.is_empty():
            self.end.next = new_node
            self.end = new_node
        else:
            self.start = self.end = new_node
        self.size += 1
        return self.size

    def delete_from_start(self):
        if not self.is_empty():
            data = self.start.data
            self.start = self.start.next
            if self.start is None:
                self.end = None
            self.size -= 1
            return data
        else:
            return None

    def delete_from_end(self):
        if not self.is_empty():
            if self.size >= 2:
                last = self.end
                current = self.start
                while current.next != last:
                    current = current.next
                self.end = current
                current.next = None
            else:
                self.start = self.end = None
            self.size -= 1
            return last.data
        else:
            return None

    def is_member(self, key):
        if not self.is_empty():
            current = self.start
            while current is not None:
                if current.data == key:
                    break
                else:
                    current = current.next
            return current is not None
        else:
            return None

    def add_after_node(self, key, value):
        new_node = self.Node(value)
        if not self.is_empty():
            current = previous = self.start
            while current is not None:
                if current.data == key:
                    previous = current
                    if current.next is not None:
                        current = current.next
                        previous.next = new_node
                        new_node.next = current
                        self.size += 1
                        break
                    else:
                        current.next = new_node
                        self.end = new_node
                        self.size += 1
                        break
                else:
                    current = current.next
        else:
            self.start = self.end = new_node
            self.size += 1
        return self.size

    def add_at_position(self, value, position):
        new_node = self.Node(value)
        count = 1
        if not self.is_empty():
            current = self.start
            while count < position:
                previous = current
                if current is not None:
                    current = current.next
                    count += 1
            if 1 <= position <= self.size and position != 1:
                previous.next = new_node
                new_node.next = current
                self.size += 1
            elif position == 1:
                new_node.next = self.start
                self.start = new_node
                self.size += 1
        else:
            self.start = self.end = new_node
            self.size += 1
        return self.size

    def add_before_node(self, key, value):
        new_node = self.Node(value)
        if not self.is_empty():
            current = previous = self.start
            while current is not None:
                if current.data == key:
                    if current != self.start:
                        previous.next = new_node
                        new_node.next = current
                        self.size += 1
                        break
                    else:
                        new_node.next = current
                        self.start = new_node
                        self.size += 1
                        break
                else:
                    previous = current
                    current = current.next
        else:
            self.start = self.end = new_node
            self.size += 1
        return self.size

    def delete_after_node(self, key):
        if not self.is_empty():
            current = self.start
            while current is not None:
                if current.data == key:
                    temp = current.next
                    if temp is not None:
                        next_node = temp.next
                        if next_node is not None:
                            current.next = next_node
                            self.size -= 1
                            break
                        else:
                            current.next = None
                            self.end = current
                            self.size -= 1
                            break
                    else:
                        return None
                else:
                    current = current.next
        else:
            return None
        return temp.data

    def delete_at_position(self, position):
        if not self.is_empty():
            current = self.start
            last_node = self.end
            count = 1
            if position <= self.size:
                while count < position:
                    previous = current
                    current = current.next
                    count += 1
                if current == self.start:
                    self.start = current.next
                    self.size -= 1
                elif current != last_node:
                    temp = current.next
                    previous.next = temp
                    self.size -= 1
                elif current == last_node:
                    previous.next = None
                    self.end = previous
                    self.size -= 1
                return current.data
            else:
                return None
        else:
            return None

    def delete_node(self, key):
        if not self.is_empty():
            current = self.start
            while current is not None:
                if current.data == key:
                    if current == self.end:
                        previous.next = None
                        self.end = previous
                        self.size -= 1
                        break
                    elif current == self.start:
                        self.start = self.start.next
                        self.size -= 1
                        break
                    else:
                        temp = current.next
                        previous.next = temp
                        self.size -= 1
                        break
                else:
                    previous = current
                    current = current.next
            return current.data
        else:
            return None

    def delete_before_node(self, key):
        if not self.is_empty():
            current = previous = self.start
            while current is not None and current.data != key:
                before = previous
                previous = current
                current = current.next
            if current is not None:
                if current != self.start and previous != self.start:
                    before.next = current
                    self.size -= 1
                    return previous.data
                elif current != self.start and previous == self.start:
                    self.start = current
                    self.size -= 1
                    return previous.data
            else:
                return None
        else:
            return None

    def get_elements(self):
        elements_list = []
        if not self.is_empty():
            current = self.start
            while current is not None:
                elements_list.append(current.data)
                current = current.next
            return elements_list


custom_list = CustomLinkedList()
custom_list.add_to_start(10)
custom_list.add_to_end(20)
custom_list.add_to_start(5)
custom_list.add_after_node(10, 15)
assert custom_list.get_elements() == [5, 10, 15, 20]
custom_list.add_after_node(20, 25)
assert custom_list.get_elements() == [5, 10, 15, 20, 25]
assert custom_list.delete_from_start() == 5
assert custom_list.delete_from_end() == 25
assert custom_list.get_elements() == [10, 15, 20]
custom_list.add_to_start(5)
assert custom_list.add_after_node(20, 25) == 5
assert custom_list.get_elements() == [5, 10, 15, 20, 25]
assert custom_list.delete_after_node(10) == 15
assert custom_list.delete_after_node(20) == 25
assert custom_list.delete_after_node(20) is None
assert custom_list.is_member(10) is True
custom_list.add_to_end(30)
assert custom_list.get_elements() == [5, 10, 20, 30]
custom_list.add_before_node(30, 25)
assert custom_list.get_elements() == [5, 10, 20, 25, 30]
custom_list.add_before_node(5, 1)
assert custom_list.get_elements() == [1, 5, 10, 20, 25, 30]
assert custom_list.add_before_node(2, 0) == 6
assert custom_list.get_elements() == [1, 5, 10, 20, 25, 30]
assert custom_list.add_at_position(0, 1) == 7
assert custom_list.get_elements() == [0, 1, 5, 10, 20, 25, 30]
assert custom_list.add_at_position(28, 7) == 8
assert custom_list.get_elements() == [0, 1, 5, 10, 20, 25, 28, 30]
assert custom_list.add_at_position(35, 9) == 8
assert custom_list.add_at_position(15, 5) == 9
assert custom_list.get_elements() == [0, 1, 5, 10, 15, 20, 25, 28, 30]
assert custom_list.delete_at_position(1) == 0
assert custom_list.get_elements() == [1, 5, 10, 15, 20, 25, 28, 30]
assert custom_list.delete_at_position(8) == 30

