# https://leetcode.com/problems/powx-n/submissions/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def my_pow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n == -1:
                return 1/x
            else:
                i = n%2
                temp = my_pow(x, n//2)
                return temp * temp * my_pow(x, i)
        
        return my_pow(x, n)