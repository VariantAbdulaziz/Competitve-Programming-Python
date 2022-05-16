# source: https://leetcode.com/problems/max-number-of-k-sum-pairs/

# policy: sorting | two pointers
class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        ans = 0
        
        while l < r:
            if nums[l] + nums[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        
        return ans