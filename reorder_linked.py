# https://leetcode.com/problems/reorder-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        alist = [0] * 50000
        
        i = 0
        temp = head
        while temp:
            alist[i] = temp.val
            temp = temp.next
            i += 1
        
        length = i
        
        temp = head
        half = length//2
        i = length - 1
        while i > half:
            temp.next = ListNode(alist[i], temp.next)
            temp = temp.next.next
            i -= 1
        
        if length % 2 != 0:
            temp.next = None
        else:
            temp.next.next = None