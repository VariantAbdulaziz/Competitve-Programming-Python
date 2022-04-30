# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head):
    
        array = []
        
        temp = head
        while temp:
            array.append(temp.val)
            temp = temp.next
        
        result = array[0] + array[len(array)-1]
        for i in range(len(array)//2):
            temp = array[i] + array[len(array)- 1 - i]
            result = temp if temp > result else result
        
        return result