# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    a_dict = {}
    temp = head
    while temp:
        if temp in a_dict:
            return 1
        a_dict[temp] = True
        temp = temp.next
    
    return 0