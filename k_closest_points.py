# solution for https://leetcode.com/problems/k-closest-points-to-origin/submissions/

class Solution:
    def eucliDistance(self, point):
        return point[0] ** 2 + point[1] ** 2
        
    def kClosest(self, points, k: int):
        
        points.sort(key=self.eucliDistance)
        
        return points[:k]