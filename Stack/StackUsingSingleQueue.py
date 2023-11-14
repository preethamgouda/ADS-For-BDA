from simpleQueue import SimpleQueue

class StackSingleQueue:
    def __init__(self):
        self.queue = SimpleQueue()

    def push(self, element):
        """Push an element onto the stack."""
        self.queue.enqueue(element)
        return self.queue.get_element_count()

    def pop(self):
        """Pop an element from the stack."""
        count = self.queue.get_element_count()
        while count > 1:
            self.queue.enqueue(self.queue.dequeue())
            count -= 1
        element = self.queue.dequeue()
        while count > 1:
            self.queue.enqueue(self.queue.dequeue())
            count -= 1
        return element

    def peek(self):
        """Get the top element of the stack without removing it."""
        count = self.queue.get_element_count()
        while count > 1:
            self.queue.enqueue(self.queue.dequeue())
            count -= 1
        element = self.queue.peek()
        self.queue.enqueue(self.queue.dequeue())
        while count > 1:
            self.queue.enqueue(self.queue.dequeue())
            count -= 1
        return element

# Test the modified class
stack_single_queue = StackSingleQueue()
stack_single_queue.push(100)
assert stack_single_queue.peek() == 100
stack_single_queue.push(200)
stack_single_queue.push(300)
stack_single_queue.push(500)
assert stack_single_queue.peek() == 500
assert stack_single_queue.pop() == 500
assert stack_single_queue.pop() == 300
assert stack_single_queue.peek() == 200
