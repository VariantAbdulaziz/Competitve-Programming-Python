# solution to https://leetcode.com/problems/find-target-indices-after-sorting-array/submissions/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # this is a two step process that needs sorting and searching
        # the result will be stored in the list below
        indicies = []
        # for the sort step i chose the insertion sort methon and it is
        # as follows
        i = 1
        while i < len(nums):
            temp = nums[i]
            j = i - 1
            while temp < nums[j] and j >= 0:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j + 1] = temp
            i += 1
        
        j = 0
        while j < len(nums) and target != nums[j]:
            j += 1
            
        while j < len(nums) and target == nums[j]:
            indicies.append(j)
            j += 1
         
        return indicies