# solution for https://leetcode.com/problems/number-of-good-pairs

from math import factorial

class Solution:
    def numIdenticalPairs(self, nums):
        freqArray = [0] * 101
        for elem in nums:
            freqArray[elem] += 1
        
        result = 0
        for elem in freqArray:
            if elem == 0 or elem == 1:
                continue
            result += factorial(elem)/(2 *(factorial(elem - 2)))
        
        return int(result)
