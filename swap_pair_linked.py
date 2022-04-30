# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        alist = [None] * 100
        
        temp = head
        i = 0
        while temp:
            alist[i] = temp
            i += 1
            temp = temp.next

        j = 1
        while j < i:
            alist[j].next = alist[j - 1]
            alist[j - 1].next = alist[j + 2]
            j += 2
        
        if j == i and j > 1:
            alist[j - 3].next = alist[j - 1]
            
            
        if alist[1]:
            return alist[1]
        elif alist[0]:
            return alist[0]
        
        return None