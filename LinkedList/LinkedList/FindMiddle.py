from singlyLinkedList import *

# Find the middle element of a linked list without iterating all elements
def find_middle_element(linked_list):
    k = linked_list.list_count() // 2
    current = linked_list.head
    count = 1
    while count < k:
        current = current.next
        count += 1
    if k % 2 == 0:
        return current.data, current.next.data
    else:
        return current.data

linked_list1 = SList()
linked_list2 = SList()
for i in range(1, 8):
    linked_list1.add_at_tail(i)
assert find_middle_element(linked_list1) == 4
for i in range(4, 12):
    linked_list2.add_at_head(i)
assert find_middle_element(linked_list2) == (8, 7)
