class Solution:
    def longestSubarray(self, nums, limit):
        array_count = [1] * len(nums)
        for i in range(len(nums) - 1):
            count = 0
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= limit:
                    count += 1
                else:
                    break
            array_count[i] = count
        
        largest = 0
        for i in range(len(array_count) - 1):
            cur_sub = array_count[i]
            while cur_sub > largest:
                all_cool = True
                count = i
                for j in range(count+1, count+cur_sub):
                    if cur_sub - array_count[j] > j - count:
                        all_cool = False
                        count += 1
                        break
                if all_cool and cur_sub > largest:
                    largest = cur_sub
                    break
                cur_sub -= 1
                    
        return largest + 1