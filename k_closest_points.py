# solution for https://leetcode.com/problems/k-closest-points-to-origin/submissions/
# for this particular question i chose bubble sort as it will allow me
# to stop sorting half way through - i,e, until the specified k
# also i want to make the sort backward in order for the smallest numbers
# to build up at the start


class Solution:
    def eucliDistance(self, point):
        return point[0] ** 2 + point[1] ** 2
        
    def kClosest(self, points, k: int):
        
        points.sort(key=self.eucliDistance)
        
        return points[:k]