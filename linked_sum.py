class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        sum_head = ListNode()
        remain = 0
        cur_sum = sum_head
        before_cur  = None
        while l1 != None or l2 != None:
            left = l1.val if l1 != None else 0
            right = l2.val if l2 != None else 0

            cur_sum.val = remain + (left + right) % 10
            cur_sum.next = ListNode()
            cur_sum.next.val = remain = (left + right) // 10
            before_cur = cur_sum
            cur_sum = cur_sum.next

            l1 = l1.next
            l2 = l2.next

        if remain == 0:
            before_cur.next = None
            
        return sum_head

l1 = ListNode(3)

l2 = ListNode(4)
sum = addTwoNumbers(l1, l2)

while sum != None:
    print(sum.val)
    sum = sum.next