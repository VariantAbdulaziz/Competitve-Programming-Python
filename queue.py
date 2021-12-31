# solution for https://leetcode.com/problems/implement-queue-using-stacks/submissions/

class MyQueue:

    def __init__(self):
        self.flipped=[]
        self.notFlipped=[]

    def push(self, x: int) -> None:
        self.flipped.append(x)
        for i in range(len(self.notFlipped)):
            self.flipped.append(self.notFlipped.pop())
        
        self.notFlipped.append(x)
        for i in range(len(self.flipped)//2):
            self.notFlipped.append(self.flipped.pop())

    def pop(self) -> int:
        self.notFlipped.pop()
        for i in range(len(self.flipped)-1):
            self.notFlipped.append(self.flipped.pop())
        
        popped = self.flipped.pop()
        for i in range(len(self.notFlipped)//2):
            self.flipped.append(self.notFlipped.pop())
        
        return popped

    def peek(self) -> int:
        return self.notFlipped[-1]

    def empty(self) -> bool:
        return 0 == len(self.flipped)
        