class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        alist = [i for i in range(1, n+1)]
        
        current = 0
        while len(alist) > 1:
            current = (current + k - 1) % len(alist)
            alist.pop(current)
            
        return alist.pop(0)