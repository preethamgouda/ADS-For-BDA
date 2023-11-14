class CircularQueueModified:
    def __init__(self):
        self.size = 0
        # Setting the size of the queue
        self.elements = [None] * 5
        self.front_index = -1
        self.rear_index = -1

    def isQueueFull(self):
        return self.size >= len(self.elements)  # Checking if the queue is full

    def isQueueEmpty(self):
        return self.size == 0

    def getCount(self):
        return self.size  # Getting the number of elements in the queue

    def enqueue(self, element):
        if not self.isQueueFull():  # Checking if the queue is full
            self.front_index = (self.front_index + 1) % len(self.elements)
            self.elements[self.front_index] = element
            self.size += 1
            return self.size
        else:
            return None

    def dequeue(self):
        if not self.isQueueEmpty():
            self.size -= 1
            self.rear_index = (self.rear_index + 1) % len(self.elements)
            item = self.elements[self.rear_index]
            self.resize(self.elements, self.rear_index, self.front_index)
            return item
        else:
            return None

    def peek(self):
        if not self.isQueueEmpty():
            return self.elements[0]
        else:
            return None

    def printElements(self):
        result_list = []
        for i in (self.elements):
            if i is not None:
                result_list.append(i)
        return result_list

    def resize(self, queue, rear, front):
        old_data = queue.copy()
        for i in range(rear + 1):
            queue[i] = None
        for i in range(rear + 1, front + 1):
            queue[i] = old_data[i]


s3_modified = CircularQueueModified()

# Enqueue 5 elements
assert s3_modified.enqueue(20) == 1
assert s3_modified.enqueue(30) == 2
assert s3_modified.enqueue(40) == 3
assert s3_modified.enqueue(50) == 4
assert s3_modified.enqueue(60) == 5

# Check queue is full
assert s3_modified.isQueueFull() is True

# Check the count of elements
assert s3_modified.getCount() == 5

# Check the front element
assert s3_modified.peek() == 20

# Dequeue an element
assert s3_modified.dequeue() == 20

# Check the count after dequeue
assert s3_modified.getCount() == 4

# Check the elements after dequeue
assert s3_modified.printElements() == [30, 40, 50, 60]

# Enqueue another element
assert s3_modified.enqueue(10) == 5

# Check the elements after enqueue
assert s3_modified.printElements() == [10, 30, 40, 50, 60]

