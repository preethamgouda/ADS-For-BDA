from singlyLinkedList import *

# Find the sum of last ‘n’ nodes in a single linked list. Where ‘n’ will be given.
# Sum should be calculated with one iteration.
def calculate_sum_of_last_n_nodes(linked_list, n):
    k = linked_list.list_count() - n + 1
    current = linked_list.head
    count = 1
    while count < k:
        current = current.next
        count += 1
    total_sum = 0
    while current is not None:
        total_sum += current.data
        if current is not None:
            current = current.next
    return total_sum

linked_list1 = SList()
linked_list2 = SList()
for i in range(1, 8):
    linked_list1.add_at_tail(i)
assert calculate_sum_of_last_n_nodes(linked_list1, 4) == 22
for i in range(4, 12):
    linked_list2.add_at_head(i)
assert calculate_sum_of_last_n_nodes(linked_list2, 5) == 30
