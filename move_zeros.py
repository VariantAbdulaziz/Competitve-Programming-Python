# https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        zero = 0
        
        while zero < len(nums) and non_zero < len(nums):
            nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
            
            while zero < len(nums) and nums[zero] != 0:
                zero += 1
            
            non_zero = zero
            while non_zero < len(nums) and nums[non_zero] == 0:
                non_zero += 1
        