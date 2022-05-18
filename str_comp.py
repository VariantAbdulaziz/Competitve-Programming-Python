# source: https://leetcode.com/problems/string-compression/

# policy: two pointers
class Solution:
    def compress(self, chars):
        l = 0
        r = 1
        prev = chars[0]
        count = 1
        while(r <= len(chars)):
            if r < len(chars) and chars[r] == prev:
                count += 1
            elif (r == len(chars) or chars[r] != prev):
                chars[l] = prev
                if count > 1:
                    s_count = str(count)
                    for digit in s_count:
                        l += 1
                        chars[l] = digit
                    l += 1
                else:
                    l += 1
                count = 1
                prev = chars[r] if r < len(chars) else ""
            r+=1
                
        return l