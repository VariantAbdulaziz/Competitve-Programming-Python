# solution to https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #  we can do this problem making use of counting sort
        aHash = [0, 0, 0]
        
        for elem in nums:
            aHash[elem] += 1
        
        i = color = 0
        while color < 3:
            count = aHash[color]
            while count > 0:
                nums[i] = color
                count -= 1
                i += 1
            color += 1
        
        
        