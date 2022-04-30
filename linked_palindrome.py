# https://leetcode.com/problems/palindrome-linked-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        stack = []
        
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        
        temp = head
        half = length // 2
        i = 0
        while i < half:
            stack.append(temp)
            temp = temp.next
            i += 1
        
        if length % 2 != 0:
            temp = temp.next
        
        while temp and stack and stack[-1].val == temp.val:
            temp = temp.next
            stack.pop()
            
        return len(stack) == 0