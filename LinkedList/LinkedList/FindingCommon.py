from singlyLinkedList import *

def find_common_elements(list1, list2, result_list):
    current_node_list1 = list1.head
    while current_node_list1:
        current_node_list2 = list2.head
        while current_node_list2:
            if current_node_list1.data == current_node_list2.data:
                result_list.addAtTail(current_node_list1.data)
            current_node_list2 = current_node_list2.next
        current_node_list1 = current_node_list1.next
    return result_list.getElements()

linked_list1 = SList()
linked_list2 = SList()
result_linked_list = SList()

for i in range(10, 16):
    linked_list1.addAtTail(i)
for i in range(13, 21):
    linked_list2.addAtHead(i)

assert find_common_elements(linked_list1, linked_list2, result_linked_list) == [13, 14, 15]
