# source: https://leetcode.com/problems/find-pivot-index/

# strategy: prefix sum
class Solution:
    def pivotIndex(self, nums):
        nums_sum = 0
        for num in nums:
            nums_sum += num
        
        prefix_sum = 0
        for i in range(len(nums)):
            if prefix_sum == nums_sum - prefix_sum - nums[i]:
                return i
            prefix_sum += nums[i]
            
        return -1