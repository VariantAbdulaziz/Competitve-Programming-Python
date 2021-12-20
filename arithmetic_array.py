# solution to https://leetcode.com/problems/arithmetic-subarrays/submissions/

class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        results = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i] + 1]
            temp.sort()
            d = temp[1] - temp[0]
            result = True
            for i in range(len(temp) - 1):
                result = d == temp[i+1] - temp[i]
                if not result:
                    break
            results.append(result)
            
        return results
        