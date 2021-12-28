# solution for https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/submissions/

class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums)//2):
            result.append(nums[len(nums)//2 + i])
            result.append(nums[i])
        
        if len(nums) % 2 != 0:
            result.append(nums[-1])
            
        return result