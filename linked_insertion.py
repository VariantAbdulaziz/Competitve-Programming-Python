# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head):
        fict_head = ListNode()
        fict_head.next = head
        cur = head.next
        while cur:
            temp = fict_head
            while temp.next != cur and temp.next.val <= cur.val:
                temp = temp.next
                
            if temp.next == cur:
                cur = cur.next
            else:
                switch = temp
                switch_next = switch.next
                cur_next = cur.next
                while temp.next != cur:
                    temp = temp.next
                
                switch.next = cur
                temp.next = cur_next
                cur.next = switch_next
                cur = cur_next
            temp = fict_head
            while temp:
                print(temp.val)
                temp = temp.next
                
        return fict_head.next

