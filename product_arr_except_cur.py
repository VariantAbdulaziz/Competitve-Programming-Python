# source: https://leetcode.com/problems/product-of-array-except-self/submissions/

# strategy: prefix/postfix product?
from itertools import accumulate


class Solution:
    def productExceptSelf(self, nums):
        left = list(accumulate(nums, lambda x, y: x*y))
        right = list(accumulate(nums[::-1], lambda x, y: x*y))[::-1]
        
        ans = [right[1]]
        for i in range(1, len(nums)-1):
            ans.append(left[i-1]*right[i+1])
        
        ans.append(left[-2])
        return ans