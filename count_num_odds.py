# source: https://leetcode.com/problems/count-number-of-nice-subarrays/

# strategy: prefix sum
class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        odd = 0
        count = 0

        for i in range(len(nums)):
            prefix[odd] += 1

            if nums[i] % 2 != 0:
                odd += 1

            if (odd >= k):
                count += prefix[odd - k]

        return count