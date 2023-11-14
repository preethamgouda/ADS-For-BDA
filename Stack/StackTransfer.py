from stack_modified import StackModified  # Assuming you have a modified stack implementation

stack1 = StackModified()
stack2 = StackModified()

def transfer(source_stack, target_stack):
    # A temporary stack is created for storing the data from source_stack
    # while copying to target_stack to maintain the same order of data
    temp_stack = StackModified()
    while source_stack.get_count() > 0:
        temp_stack.push(source_stack.pop())
    while temp_stack.get_count() > 0:
        target_stack.push(temp_stack.pop())
    return target_stack.print_elements()

stack1.push(100)
stack1.push(200)
stack1.push(300)
stack1.push(400)
assert transfer(stack1, stack2) == [100, 200, 300, 400]
