# https://docs.google.com/spreadsheets/d/1r3VHGkWFz5p307GjmxoOG44YpQdSyasfnTea0-AtX1E/edit#gid=1107991618

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head):
        result = []
        mon_stack = []
        temp = head
        i = 0
        while temp:
            result.append(0)
            
            while mon_stack and temp.val > mon_stack[-1][0]:
                result[mon_stack.pop()[1]] = temp.val
            
            mon_stack.append((temp.val, i))
            
            i += 1
            temp = temp.next
        
        return result