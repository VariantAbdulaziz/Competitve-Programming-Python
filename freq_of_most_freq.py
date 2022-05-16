# source: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        preSum = []
        preSum.append(0)
        for num in nums:
            preSum.append(preSum[-1] + num)
        
        freq = 0
        l = 0
        r = 0
        
        while r < len(preSum):
            if (nums[r-1] * (r - l)) - (preSum[r] - preSum[l])  <= k:
                freq = max(freq, r - l)
                r += 1
            else:
                l += 1
                
        return freq