# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        while cur and cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        if cur:
            cur.next = prev
        return cur