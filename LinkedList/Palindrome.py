from singlyLinkedList import *
from reverse import *

# Function to check if a given linked list is a palindrome
def is_palindrome(linked_list):
    return linked_list.get_elements() == reverse_linked_list(linked_list)

linked_list1 = SList()
for i in range(1, 8):
    linked_list1.add_at_tail(i)
assert not is_palindrome(linked_list1)  # This linked list is not a palindrome

linked_list2 = SList()
characters = ['M', 'A', 'L', 'A', 'Y', 'A', 'L', 'A', 'M']
for char in characters:
    linked_list2.add_at_tail(char)
assert is_palindrome(linked_list2)  # This linked list is a palindrome
