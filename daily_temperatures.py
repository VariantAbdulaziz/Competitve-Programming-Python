class Solution:
    def dailyTemperatures(self, temperatures):
        
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 2, -1, -1):
            index = i + 1
            while True:
                if temperatures[index] <= temperatures[i] and result[index] != 0:
                    index = index + result[index]
                elif temperatures[index] > temperatures[i]:
                    result[i] = index - i
                    break
                elif result[index] == 0:
                    result[i] = 0
                    break
                
                    
        return result