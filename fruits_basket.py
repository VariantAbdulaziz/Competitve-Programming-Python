# source: https://leetcode.com/problems/fruit-into-baskets

# strategy: two pointers
class Solution:
    def totalFruit(self, fruits):
        l = [fruits[0], -1] # fruit, index
        r = [-1, -1]
        res = 1
        for i in range(len(fruits)):
            if fruits[i] != l[0] and fruits[i] != r[0]:
                r = l
                l = [fruits[i], i - 1]
            elif fruits[i] != l[0]:
                r[0] = l[0]
                l = [fruits[i], i - 1]

            res = max(res, i - r[1])
            
        return res