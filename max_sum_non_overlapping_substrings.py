# source: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

# strategy: two pointers | sliding window | two fronts
class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:
        lf, rs, ls, rf = 0, 0, 0, 0
        
        for i in range(firstLen):
            lf += nums[i]
            
        for i in range(firstLen, firstLen+secondLen):
            ls += nums[i]
            
        for i in range(-1, -firstLen - 1, -1):
            rf += nums[i]
            
        for i in range(-firstLen - 1, -firstLen - secondLen - 1, -1):
            rs += nums[i]
        
        lm, rm= lf, rf
        res  = max(rm + rs, lm + ls)
        for i in range(firstLen + secondLen, len(nums)):
            lf += nums[i - secondLen] - nums[i - firstLen - secondLen]
            ls += nums[i] - nums[i - secondLen]
            
            lm = max(lm, lf)
            res = max(res, lm + ls)
        
        res = max(res, rf + rs)
        for i in range(- firstLen - secondLen - 1, -len(nums) - 1, -1):
            rf += nums[i + secondLen] - nums[i + firstLen + secondLen]
            rs += nums[i] - nums[i + secondLen]
            
            rm = max(rf, rm)
            res = max(res, rm + rs)
            
        return res