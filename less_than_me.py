 # solution to https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        lessThanfrequencyArray = [0] * 101
        lessThanCount = [0] * len(nums)
        
        for elem in nums:
            i = elem + 1
            while i < 101:
                lessThanfrequencyArray[i] += 1
                i += 1
        
        for i in range(0, len(nums)):
            lessThanCount[i] = lessThanfrequencyArray[nums[i]]
        
        
        return lessThanCount
        