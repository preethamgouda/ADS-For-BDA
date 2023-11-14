from singlyLinkedList import SList

def remove_duplicates(linked_list):
    current = previous = linked_list.head
    unique_elements = set()

    while current is not None:
        if current.data in unique_elements:
            previous.next = current.next
            current = current.next
        else:
            unique_elements.add(current.data)
            previous = current
            current = current.next

    return linked_list.get_elements()


list1 = SList()
list2 = SList()

for i in range(10, 21):
    list1.add_at_tail(i)

assert remove_duplicates(list1) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(5, 16):
    list2.add_at_tail(i)

for i in range(21, 31):
    list2.add_at_tail(i)

for i in range(1, 6):
    list2.add_at_head(i)

assert remove_duplicates(list2) == [5, 4, 3, 2, 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
