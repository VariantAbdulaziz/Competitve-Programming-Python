# solution for https://leetcode.com/problems/k-closest-points-to-origin/submissions/

# for this particular question i chose bubble sort as it will allow me
# to stop sorting half way through - i,e, until the specified k
# also i want to make the sort backward in order for the smallest numbers
# to build up at the start

from math import sqrt

class Solution:
    def eucliDistance(self, points, i):
        return sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        
    def kClosest(self, points, k):
        kClosestPoints = [0] * k
        
        i = 0
        while i < k:
            j = len(points) - 1
            while j > i:
                if self.eucliDistance(points, j) < self.eucliDistance(points, j-1):
                    points[j], points[j - 1] = points[j -1], points[j]
                j -= 1
            kClosestPoints[i] = points[i]
            i += 1
        
        return kClosestPoints