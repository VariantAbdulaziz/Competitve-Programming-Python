# source: https://leetcode.com/problems/longest-substring-without-repeating-characters

# policy: two pointers | slidding window | map
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        adict = {}
        l = -1
        r = 0
        res = 0
        for letter in s:
            if letter in adict:
                l = max(l, adict[letter])
            res = max(res, r - l)
            adict[letter] = r
            r+=1
            
        return res
        