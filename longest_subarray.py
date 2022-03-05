class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        largest = 1
        upBound = limit
        lowerBound = 0
        queue = []
        for elem in nums:
            queue.append(elem)
            if elem > upBound:
                upBound = elem
                lowerBound = upBound - limit
                for i in range(len(queue)-1, -1, -1):
                    if queue[i] < lowerBound:
                        queue = queue[i+1:]
                        break   
            elif elem < lowerBound:
                lowerBound = elem
                upBound = lowerBound + limit
                i = len(queue) - 2
                for i in range(len(queue)-1, -1, -1):
                    if queue[i] > upBound:
                        queue = queue[i+1:]
                        break  
            if len(queue) > largest:
                largest = len(queue)
        return largest