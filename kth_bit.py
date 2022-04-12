class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s = list(s)
            for i in range(len(s)):
                s[i] = '0' if s[i] == '1' else '1'
            return ''.join(s)
        
        def form_binary(n):
            if n == 1:
                return '0'
            else:
                temp = form_binary(n - 1)
                return temp + '1' + invert(temp)[::-1]
            
        s = form_binary(n)
        
        return s[k -1]