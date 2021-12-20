# solution to https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/

class Solution:
    def maxCoins(self, piles):
        
        piles.sort(reverse = True)
        
        result = 0
        for i in range(0, 2 * len(piles)//3, 2):
            result += piles[i + 1]
            
        return result