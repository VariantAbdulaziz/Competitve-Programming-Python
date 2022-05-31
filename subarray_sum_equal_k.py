# source: https://leetcode.com/problems/subarray-sum-equals-k/submissions/

# strategy: prefix sum
from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        book = defaultdict(lambda: 0)
        
        ans = 0
        pre_sum = 0
        book[pre_sum]+=1
        for i in range(len(nums)):
            pre_sum += nums[i]
            
            if pre_sum - k in book:
                ans+=book[pre_sum - k]
            
            book[pre_sum]+=1
        
        return ans