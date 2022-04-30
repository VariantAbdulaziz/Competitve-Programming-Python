# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        for i in range(len(s)):
            alist = [False] * 100
            alist[ord(s[i]) - 65] = True
            sub_len = 1
            for j in range(i+1, len(s)):
                index = ord(s[j]) - 65
                if alist[index]:
                    break
                else:
                    alist[index] = True
                    sub_len += 1
            
            result = sub_len if sub_len > result else result
            
        return result