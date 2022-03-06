class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        mon_queue = []
        for citation in citations:
            if citation >= len(mon_queue):
                mon_queue.append(citation)
                while True:
                    if mon_queue and mon_queue[0] < len(mon_queue):
                        mon_queue.pop(0)
                    else:
                        break
        
        return len(mon_queue)