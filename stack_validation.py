class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        while True:
            if stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            elif pushed:
                stack.append(pushed.pop(0))
            else:
                break
        
        if stack or popped or pushed:
            return False
        return True