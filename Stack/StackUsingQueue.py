from simpleQueue_modified import SimpleQueueModified  # Assuming you have a modified queue implementation

class StackUsingQueue:
    def __init__(self):
        self.queue1 = SimpleQueueModified()
        self.queue2 = SimpleQueueModified()

    def push_new(self, element):
        """Enqueuing the element to the queue is the same as pushing the element to the stack."""
        return self.queue1.enqueue(element)

    def pop_new(self):
        """Popping the element from the stack should give the top element,
        but dequeue operation will give the rear element.
        Dequeue element from queue1 and enqueue to queue2 until the last element found.
        The last element is popped.
        Again all elements from queue2 will be enqueued back to queue1."""
        while self.queue1.get_element_count() > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        element = self.queue1.dequeue()
        while self.queue2.get_element_count() > 0:
            self.queue1.enqueue(self.queue2.dequeue())
        return element

    def peek_new(self):
        """Get the top element of the stack without removing it."""
        while self.queue1.get_element_count() > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        element = self.queue1.peek()
        self.queue2.enqueue(self.queue1.dequeue())
        while self.queue2.get_element_count() > 0:
            self.queue1.enqueue(self.queue2.dequeue())
        return element

# Test the modified class
stack_using_queue = StackUsingQueue()
assert stack_using_queue.push_new(5) == 1
assert stack_using_queue.push_new(15) == 2
assert stack_using_queue.push_new(25) == 3
assert stack_using_queue.pop_new() == 25
assert stack_using_queue.peek_new() == 15
