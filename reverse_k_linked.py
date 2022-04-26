# https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):
        
        prev = None
        cur = head
        while cur:
            temp_k = k - 1
            temp = ListNode(cur.val)
            prev_candidate = temp
            back_up = cur
            cluster_prev = temp
            cur = cur.next
            while temp_k > 0 and cur:
                tempest = ListNode(cur.val, temp)
                temp = tempest
                cur = cur.next
                temp_k -=1
            
            if prev:
                if temp_k == 0:
                    prev.next = temp
                    prev = prev_candidate
                else:
                    prev.next = back_up
            else:
                if temp_k == 0:
                    head = temp
                    prev = prev_candidate
                else:
                    prev = back_up
                    
            
        return head