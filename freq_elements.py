# solution to https://leetcode.com/problems/top-k-frequent-elements/submissions/

class Solution:
    def rangeComp(self, tup):
        return tup[1]
    def topKFrequent(self, nums, k):
        nums.sort()
        freqArray = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            freqArray.append((nums[i], j - i))
            i = j
        
        freqArray.sort(reverse=True, key=self.rangeComp)
        
        return [elem[0] for elem in freqArray[:k]]
            