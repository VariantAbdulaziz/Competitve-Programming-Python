# https://leetcode.com/problems/design-linked-list/submissions/

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        
        if index >= self.len:
            return -1
        
        temp = self.head
        i = 0
        while i < index:
            temp = temp.next
            i += 1
            
        return temp.val
        

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.len += 1
        
        

    def addAtTail(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
            self.len += 1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = Node(val)
            self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len:
            self.addAtTail(val)
        elif index < 1:
            self.addAtHead(val)
        elif index > self.len:
            pass
        else:
            i = 0
            temp = Node(0, self.head)
            while i < index:
                i += 1
                temp = temp.next

            temp.next = Node(val, temp.next)
            self.len += 1
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index == 0:
            self.head = self.head.next
            self.len -= 1
        elif index < self.len:
            i = 1
            temp = self.head
            while i < index:
                i += 1
                temp = temp.next

            temp.next = temp.next.next
            self.len -= 1