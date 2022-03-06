class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                continue
            else:
                result += nums[i-1] - nums[i] + 1
                nums[i] += nums[i-1] - nums[i] + 1
        
        return result