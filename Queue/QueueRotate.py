from simpleQueue_modified import SimpleQueueModified  
from stack_modified import StackModified  

class RotateQueue:
    # Contents of queue can be rotated using a stack
    def __init__(self):
        self.queue = SimpleQueueModified()
        self.stack = StackModified()

    def rotate_method_using_stack(self):
        while self.queue.get_element_count() > 0:
            self.stack.push(self.queue.dequeue())
        while self.stack.get_count() > 0:
            self.queue.enqueue(self.stack.pop())
        return self.queue.print_elements()

# Test the modified class
rotate_queue = RotateQueue()
rotate_queue.queue.enqueue(5)
rotate_queue.queue.enqueue(10)
rotate_queue.queue.enqueue(15)
rotate_queue.queue.enqueue(20)
assert rotate_queue.rotate_method_using_stack() == [20, 15, 10, 5]
