class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k + 1
        self.deque = [0] * self.capacity
        self.front = 0
        self.back = 0

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            
            self.deque[ (self.front - 1) % self.capacity] = value
            self.front = (self.front - 1)% self.capacity
            return True
        else:
            return False
    
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            
            self.deque[ self.back ] = value
            self.back = (self.back + 1)%self.capacity
        
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            
            self.front = (self.front+1)%self.capacity
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.back = (self.back-1)%self.capacity
            return True
        
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[ (self.front)%self.capacity]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[(self.back - 1)%self.capacity]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.front == self.back

    def isFull(self) -> bool:
        return self.front == (self.back + 1)%self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()