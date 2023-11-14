class SList:
    class Node:
        def __init__(self, ele):
            self.data = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.max = float('-inf')  # Initialize max to negative infinity

    def is_empty(self):
        return self.count == 0

    def list_count(self):
        return self.count

    def max_element(self):
        return self.max

    def add_at_head(self, ele):
        new_node = self.Node(ele)
        if not self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1
        self.update_max(new_node.data)
        return self.count

    def add_at_tail(self, ele):
        new_node = self.Node(ele)
        if not self.is_empty():
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1
        self.update_max(new_node.data)
        return self.count

    def update_max(self, data):
        if data > self.max:
            self.max = data


slist = SList()
slist.add_at_head(10)
assert slist.max_element() == 10
slist.add_at_tail(20)
slist.add_at_head(5)
assert slist.max_element() == 20
