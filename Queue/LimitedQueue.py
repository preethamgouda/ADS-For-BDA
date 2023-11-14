class LimitedQueue:
    def __init__(self):
        self.count = 0
        # Setting the size of the queue
        self.data = [None] * 5
        self.front = -1

    def is_queue_full(self):
        return self.count >= len(self.data)  # Checking if queue is full

    def is_queue_empty(self):
        return self.count == 0

    def get_count(self):
        return self.count  # Getting the number of elements in the queue

    def enqueue(self, element):
        if not self.is_queue_full():  # Checking if queue is full
            self.front += 1  # If the queue is not full, then increment the front and enqueue the element in the index of front
            self.data[self.front] = element
            self.count += 1
            return self.count
        else:
            return None

    def dequeue(self):
        if not self.is_queue_empty():
            self.count -= 1
            return self.data.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_queue_empty():
            return self.data[0]
        else:
            return None

    def print_elements(self):
        return self.data


# Test the modified class
limited_q = LimitedQueue()
assert limited_q.enqueue(10) == 1
assert limited_q.enqueue(20) == 2
assert limited_q.enqueue(30) == 3
assert limited_q.dequeue() == 10
assert limited_q.peek() == 20
assert limited_q.print_elements() == [20, 30]
