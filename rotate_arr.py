# source: https://leetcode.com/problems/rotate-array/

# strategy: book keeping | two pointers
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        r = len(nums) - k
        book = []
        while r < len(nums):
            book.append(nums[r])
            r +=1
        
        l = len(nums) - k - 1
        r = len(nums) - 1
        while l > -1:
            nums[r] = nums[l]
            l -= 1
            r -= 1
        
        l = 0
        while l < k:
            nums[l] = book.pop(0)
            l += 1