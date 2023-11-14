from stack_modified import StackModified  

class QueueUsingStack:
    def __init__(self):
        # Initializing 2 stacks
        self.stack1 = StackModified()
        self.stack2 = StackModified()

    def enqueue_new(self, element):
        # Enqueuing to the queue is the same as pushing the element to the stack
        # using the push function used in the stack
        self.stack1.push(element)
        return self.stack1.get_count()

    def dequeue_new(self):
        # To dequeue an element we need to get the rear element, but in the stack, we can have only the top element
        # pop element from the stack until we find the last element and push it to the new stack (stack2).        while 	

	self.stack1.get_count() > 1:
            self.stack2.push(self.stack1.pop())
        element = self.stack1.pop()
        while self.stack2.get_count() > 0:
            self.stack1.push(self.stack2.pop())
        return element

    def peek_new(self):
        while self.stack1.get_count() > 1:
            self.stack2.push(self.stack1.pop())
        element = self.stack1.peek()
        self.stack2.push(self.stack1.pop())
        while self.stack2.get_count() > 0:
            self.stack1.push(self.stack2.pop())
        return element

# Test the modified class with different numbers
q1 = QueueUsingStack()
assert q1.enqueue_new(8) == 1
assert q1.enqueue_new(16) == 2
assert q1.enqueue_new(24) == 3
assert q1.dequeue_new() == 8
assert q1.peek_new() == 16
