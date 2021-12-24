# solution to https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/submissions/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        aList = []
        for elem in s:
            
            if elem != ')':
                aList.append(elem)
            else:
                sList = []
                temp = aList.pop()
                while temp != '(':
                    sList.append(temp)
                    temp = aList.pop()
                
                for token in sList:
                    aList.append(token)
        
        result = ''
        while len(aList) > 0:
            result += aList.pop(0)
            
        return result
                    
                    