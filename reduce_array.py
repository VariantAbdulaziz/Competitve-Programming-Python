# solution to https://leetcode.com/problems/reduce-array-size-to-the-half/submissions/

class Solution:
    def minSetSize(self, arr):
        arr.sort()
        freqArray = []
        i = 0
        while i < len(arr):
            j = i
            while j < len(arr) and arr[j] == arr[i]:
                j += 1
            freqArray.append(j - i)
            i = j
            
        freqArray.sort()
        result = 0
        sumFreq = 0
        while len(arr)//2 > sumFreq:
            sumFreq += freqArray.pop()
            result += 1
        
        return result