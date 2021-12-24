# solution to https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:
        aDict = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }
        aStack = []
        for elem in s:
            if elem in aDict:
                aStack.append(aDict[elem])
            elif len(aStack) != 0:
                temp = aStack.pop()
                if elem == temp:
                    continue
                else:
                    return False
            elif len(aStack) == 0:
                return False
        
        if len(aStack) == 0:
            return True
        return False