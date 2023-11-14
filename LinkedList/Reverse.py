from singlyLinkedList import *

# Function to reverse a singly linked list
def reverse_linked_list(singly_list):
    current_node = singly_list.head
    previous_node = None
    singly_list.tail = current_node

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        singly_list.head = previous_node

    return singly_list.get_elements()

linked_list = SList()

# Populating the linked list with numbers from 1 to 7
for i in range(1, 8):
    linked_list.add_at_tail(i)

# Reversing the linked list and checking the result
assert reverse_linked_list(linked_list) == [7, 6, 5, 4, 3, 2, 1]
