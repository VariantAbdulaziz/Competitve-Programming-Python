# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        count = 1
        temp = head
        while temp.next:
            count += 1
            temp = temp.next
        
        outcast_no = count - n
        
        temp = head
        prev = None
        while outcast_no > 0:
            prev = temp
            temp = temp.next
            outcast_no -= 1
        
        if prev:
            prev.next = temp.next
            temp.next = None
        else:
            head = head.next
        
        return head