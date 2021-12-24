# solution to https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums):
        nums.sort()
        
        maxPairSum = 0
        for i in range(len(nums)//2):
            currentSum = nums[i] + nums[-(i+1)]
            maxPairSum = max(maxPairSum, currentSum)
            
        return maxPairSum