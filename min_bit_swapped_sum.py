class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        def my_pow(x, n, mod):
            if n == 0:
                return 1
            elif n == 1:
                return x % mod
            else:
                temp = my_pow(x, n//2, mod)
                return temp * temp * my_pow(x, n%2, mod) % mod
             
        MOD = 10**9 + 7
        
        up_bound = 2**p - 1
        
        return up_bound * my_pow(up_bound - 1, up_bound//2, MOD) % MOD