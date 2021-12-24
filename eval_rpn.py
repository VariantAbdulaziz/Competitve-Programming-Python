# solution to https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/

class Solution:
    def operateOnem(self, a, b, o):
        if o == "+":
            return b + a
        if o == "-":
            return b - a
        if o == "*":
            return b * a
        if o == "/":
            return int(b / a)
        
    def evalRPN(self, tokens) -> int:
        aStack = []
        operators = ['*', '+', '-', '/']
        
        for token in tokens:
            if token in operators:
                aStack.append(self.operateOnem(aStack.pop(), aStack.pop(), token))
            else:
                aStack.append(int(token))
        
        return aStack[0]