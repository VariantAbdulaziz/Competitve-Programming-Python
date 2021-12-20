# solution for https://leetcode.com/problems/find-original-array-from-doubled-array/submissions/

class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        
        aDict = {}
        for elem in changed:
            if elem == 0:
                if elem not in aDict:
                    aDict[elem] = [1, 0]
                elif aDict[elem][0] < aDict[elem][1]:
                    aDict[elem//2][0] += 1
                else:
                    aDict[elem//2][1] += 1
            elif elem % 2 != 0 and elem not in aDict:
                aDict[elem] = [1, 0]
            elif elem % 2 != 0:
                aDict[elem][0] += 1
            elif elem//2 in aDict and aDict[elem//2][0] > aDict[elem//2][1]:
                aDict[elem//2][1] += 1
            elif elem not in aDict:
                aDict[elem] = [1, 0]
            elif elem in aDict:
                aDict[elem][0] += 1
        
        result = []
        
        for key in aDict.keys():
            if aDict[key][0] == aDict[key][1]:
                for i in range((aDict[key][0])):
                    result.append(key)
            else:
                return []
        
        return result
                    
                