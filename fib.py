class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _fib(n, memo):
            if n <= 1:
                if memo[n] == -1:
                    memo[n] = n
                return memo[n]
            else:
                if memo[n - 1] == -1:
                    memo[n - 1] = _fib(n - 1, memo)
                if memo[n - 2] == -1:
                    memo[n - 2] = _fib(n - 2, memo)
                return memo[n - 1] + memo[n - 2]
        
        memo = [-1] * (n + 1)
        return _fib(n, memo)