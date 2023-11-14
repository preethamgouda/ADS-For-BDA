class Stack:
    def __init__(self):
        self.size = 0  # Updated variable name
        self.items = []  # Updated variable name

    def is_empty(self):
        """Check if the stack is empty."""
        return self.size == 0

    def get_size(self):
        """Get the number of elements in the stack."""
        return self.size

    def push(self, element):
        """Push an element onto the stack."""
        self.items.append(element)
        self.size += 1
        return self.size

    def pop(self):
        """Pop an element from the stack."""
        if not self.is_empty():
            self.size -= 1
            return self.items.pop()
        else:
            return None

    def peek(self):
        """Get the top element of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def print_elements(self):
        """Print the elements of the stack."""
        return self.items
