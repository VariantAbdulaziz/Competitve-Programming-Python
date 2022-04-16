# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        
        mid = count//2 + 1
        temp = head   
        for i in range(mid - 1):
            temp = temp.next
            
        return temp