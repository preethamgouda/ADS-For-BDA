class DoublyList:
    class Node:
        def __init__(self, value):
            self.data = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def get_count(self):
        return self.count

    def add_at_head(self, value):
        new_node = self.Node(value)
        if not self.is_empty():
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1
        return self.count

    def add_at_tail(self, value):
        new_node = self.Node(value)
        if not self.is_empty():
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1
        return self.count

    def delete_at_head(self):
        if not self.is_empty():
            element = self.head.data
            temp = self.head.next
            if temp:
                temp.prev = None
                self.head = temp
            else:
                self.tail = self.head
            self.count -= 1
            return element
        else:
            return None

    def delete_at_tail(self):
        if not self.is_empty():
            element = self.tail.data
            temp = self.tail.prev
            if temp:
                temp.next = None
                self.tail = temp
            else:
                self.head = self.tail
            self.count -= 1
            return element
        else:
            return None

    def get_elements(self):
        if not self.is_empty():
            current = self.head
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            return elements
        else:
            return None

# Example usage:
dlist = DoublyList()
assert(dlist.add_at_head(100) == 1)
assert(dlist.add_at_tail(200) == 2)
assert(dlist.add_at_head(50) == 3)
assert(dlist.add_at_tail(250) == 4)
assert(dlist.get_elements() == [50, 100, 200, 250])
assert(dlist.delete_at_head() == 50)
assert(dlist.delete_at_tail() == 250)
assert(dlist.get_elements() == [100, 200])
assert(dlist.delete_at_tail() == 200)
assert(dlist.delete_at_tail() == 100)
assert(dlist.add_at_head(150) == 1)
assert(dlist.add_at_tail(200) == 2)
assert(dlist.delete_at_head() == 150)
assert(dlist.delete_at_head() == 200)
