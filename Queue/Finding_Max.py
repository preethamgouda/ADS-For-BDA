from simpleQueue_modified import SimpleQueueModified  

class FindMaxElement:
    def __init__(self):
        # Initializing 2 queues
        self.queue_1 = SimpleQueueModified()
        self.queue_2 = SimpleQueueModified()

    # Method to print the elements in the queue from rear to front
    def print_elements(self):
        return self.queue_1.print_elements()

    # Method to find the maximum element
    def find_max(self):
        max_element = float('-inf')  # Initialize max_element with negative infinity
        # We will dequeue every element from the queue, compare it with the variable maximum,
        # and if it's more than max, max will be updated with the new value.

        while self.queue_1.get_element_count() > 0:
            element = self.queue_1.dequeue()
            if max_element < element:
                max_element = element
            self.queue_2.enqueue(element)
        while self.queue_2.get_element_count() > 0:
            self.queue_1.enqueue(self.queue_2.dequeue())
        return max_element

# Different approach and asserting values
s1 = FindMaxElement()
assert s1.queue_1.enqueue(40) == 1
assert s1.queue_1.enqueue(10) == 2
assert s1.queue_1.enqueue(30) == 3
assert s1.find_max() == 40
assert s1.queue_1.dequeue() == 40
assert s1.queue_1.enqueue(60) == 4  assert s1.find_max() == 60  
