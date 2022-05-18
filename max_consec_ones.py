# source: https://leetcode.com/problems/max-consecutive-ones-iii/

# strategy: book keeping | deque | semaphores | two pointers
class Solution:
    def longestOnes(self, nums, k):
        dq = [-1]
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                dq.append(i)  
                if count == k:
                    count -= 1
                    dq.pop(0)
                count += 1
            res = max(res, i - dq[0])
        
        return res