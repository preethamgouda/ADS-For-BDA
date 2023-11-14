from stack import Stack  # Assuming you have a Stack class implemented

def reverse(file_path):
    s1 = Stack()

    # Read lines from the file and push them onto the stack
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            s1.push(line.strip())  # Remove newline characters if needed

    # Write lines from the stack back to the file in reverse order
    with open('output.txt', 'w') as output_file:
        while not s1.is_empty():
            output_file.write(s1.pop() + '\n')

# Example usage:
reverse('sample.txt')
