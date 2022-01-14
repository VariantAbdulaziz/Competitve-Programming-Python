# solution to https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:
    def __init__(self):
        self.requests = []
        self.minIndex = 0
    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        lowerRange = t - 3000
        for i in range(self.minIndex, len(self.requests)):
            if self.requests[i] >= lowerRange:
                self.minIndex = i
                break
        return len(self.requests[self.minIndex:])
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)