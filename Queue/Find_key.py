from stack_modified import StackModified  # Assuming you have a modified stack implementation
from simpleQueue_modified import SimpleQueueModified  # Assuming you have a modified queue implementation

# Program to check if the key is present in the given stack using one stack and queue
def find_key(key):
    stack_1 = StackModified()
    queue_1 = SimpleQueueModified()
    stack_1.push(10)
    stack_1.push(20)
    stack_1.push(30)
    stack_1.push(40)
    found = 0

    while stack_1.get_count() > 0:
        element = stack_1.pop()
        queue_1.enqueue(element)
        if key == element:
            found = 1

    copy_queue_to_stack(stack_1, queue_1)
    copy_stack_to_queue(stack_1, queue_1)
    copy_queue_to_stack(stack_1, queue_1)
    return found == 1

def copy_queue_to_stack(stack_1, queue_1):
    while queue_1.get_count() > 0:
        stack_1.push(queue_1.dequeue())

def copy_stack_to_queue(stack_1, queue_1):
    while stack_1.get_count() > 0:
        queue_1.enqueue(stack_1.pop())

# Different approach to asserting values
assert find_key(20) is True
assert find_key(200) is False
