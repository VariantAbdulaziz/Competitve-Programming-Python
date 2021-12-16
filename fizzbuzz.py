

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        alist = [''] * n
        i = 1
        while i <= n:
            if i % 3 == 0:
                alist[i-1] += "Fizz"
            if i % 5 == 0:
                alist[i-1] += "Buzz"
            if i % 3 != 0 and i % 5 != 0:
                alist[i-1] += str(i)
            i += 1
        return alist