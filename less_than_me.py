# solution to https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# for this particular question i chose to sort the items in a
# non decreasing order with selectin sort as it maitains the index
# that the selection is coming from 

class Solution:
    def select(self, nums, i):
        j = i + 1
        while j < len(nums):
            if nums[j] > nums[i]:
                i = j
            j += 1
            
        return i
    def smallerNumbersThanCurrent(self, nums):
        lessThanCount = [0] * len(nums)
        
        i = 0
        while i < len(nums) - 1:
            j = self.select(nums, i)
            nums[i], nums[j] = nums[j], nums[i]
            lessThanCount[j] = len(nums) - 1 - i
                
                
            i += 1
            
        return lessThanCount