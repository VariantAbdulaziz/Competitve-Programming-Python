# solution to https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def sortNumInts(self, strNum):
        return int(strNum)
        
    def kthLargestNumber(self, nums, k: int):
        
        nums.sort(key=self.sortNumInts)
        
        return nums[len(nums) - k]