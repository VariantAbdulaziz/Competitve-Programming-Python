# solution to https://leetcode.com/problems/merge-intervals/

class Solution:
    def lowerInitial(self, interval):
        return interval[0]
    
    def overlapped(self, interval_0, interval_1):
        if interval_0[0] <= interval_1[0] and interval_1[0] <= interval_0[1]:
            return True
        elif interval_1[0] <= interval_0[0] and interval_0[0] <= interval_1[1]:
            return True
        return False
        
    def merge(self, intervals):
        result = []
        intervals.sort(key=self.lowerInitial)
        result.append(intervals[0])
        i = 1
        while i < len(intervals):
            if self.overlapped(result[-1], intervals[i]):
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1
        
        return result