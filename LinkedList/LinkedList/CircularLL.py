class CircularList:
    class Node:
        def __init__(self, value):
            self.data = value
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
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
            self.tail.next = self.head
        self.count += 1
        return self.count

    def add_at_tail(self, value):
        new_node = self.Node(value)
        if not self.is_empty():
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            self.head = self.tail = new_node
            self.tail.next = self.head
        self.count += 1
        return self.count

    def delete_at_head(self):
        if not self.is_empty():
            element = self.head.data
            temp = self.head.next
            if temp != self.tail:
                self.tail.next = temp
                self.head = temp
            else:
                self.head = self.tail
            self.count -= 1
            return element
        else:
            print("None")
            return None

    def delete_at_tail(self):
        if not self.is_empty():
            element = self.tail.data
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
            self.count -= 1
            return element
        else:
            print("None")
            return None

    def get_elements(self):
        if not self.is_empty():
            current = self.head.next
            elements = []
            elements.append(self.head.data)
            while current != self.head:
                elements.append(current.data)
                current = current.next
            return elements
        else:
            return None

# Example usage:
clist = CircularList()
assert(clist.add_at_head(100) == 1)
assert(clist.add_at_tail(200) == 2)
assert(clist.add_at_head(50) == 3)
assert(clist.add_at_tail(250) == 4)
assert(clist.get_elements() == [50, 100, 200, 250])
assert(clist.delete_at_head() == 50)
assert(clist.delete_at_tail() == 250)
assert(clist.get_elements() == [100, 200])
assert(clist.delete_at_tail() == 200)
assert(clist.delete_at_tail() == 100)
assert(clist.add_at_head(150) == 1)
assert(clist.add_at_tail(200) == 2)
assert(clist.delete_at_head() == 150)
assert(clist.delete_at_head() == 200)
