# solution to https://leetcode.com/problems/pancake-sorting/solution/

class Solution:
    def reverse(self, arr, i):
        for j in range(i//2):
            arr[j], arr[i-1-j] = arr[i-1-j], arr[j]
            
    def pancakeSort(self, arr):
        result = []
        for i in range(len(arr), 0, -1):
            indexOfMax = arr.index(i, 0, i)
            result.append(indexOfMax + 1)
            result.append(i)
            self.reverse(arr, indexOfMax + 1)
            self.reverse(arr, i)
        return result