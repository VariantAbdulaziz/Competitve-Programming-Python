# https://leetcode.com/problems/largest-number/submissions/

class Solution:
    class Node:
        def __init__(self, num):
            self.num = str(num)
        
        def __lt__(self, value):
            return self.num + value.toString() < value.toString() + self.num
                
                
        def toString(self):
            return self.num
                           
    def largestNumber(self, nums) -> str:
        def nodalize(num):
            return self.Node(num)
        
        nums = list(map(nodalize, nums))
        
        nums.sort(reverse=True)
        result = ''
        for elem in nums:
            result += elem.toString()
        
        
       
        return str(int(result))