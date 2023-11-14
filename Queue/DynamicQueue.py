class DynamicQueue:
    default_size = 2

    def __init__(self):
        # Setting the default size of the queue
        self.data = [None] * DynamicQueue.default_size
        self.front = 0
        self.count = 0

    # Method to get the number of elements in the queue
    def length(self):
        return self.count

    # Method to check if the queue is empty
    def is_empty(self):
        return self.count == 0

    # Method to get the first element in the queue
    def get_first(self):
        if not self.is_empty():
            return self.data[self.front]
        else:
            return None

    def enqueue(self, element):
        # Condition to check if the queue is full, if it's full resizing the queue
        if self.count == len(self.data):
            self.resize(2 * len(self.data))
        index = (self.front + self.count) % len(self.data)
        self.data[index] = element
        self.count += 1
        return self.count

    def dequeue(self):
        if not self.is_empty():
            element = self.data[self.front]
            self.count -= 1
            self.data[self.front] = None
            # Again shrinking the queue size once deleting the element
            self.front = (self.front + 1) % len(self.data)
            if 0 < len(self.data) // 4:
                self.resize(len(self.data) // 2)
            return element
        else:
            return None

    def resize(self, capacity):
        old_data = self.data
        walk = self.front
        self.data = [None] * capacity
        for k in range(self.count):
            self.data[k] = old_data[walk]
            walk = (walk + 1) % len(old_data)
        self.front = 0

    def get_size(self):
        return len(self.data)
