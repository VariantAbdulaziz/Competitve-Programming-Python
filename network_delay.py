# source: https://leetcode.com/problems/network-delay-time/

# strategy: dijkstra
import collections
import heapq


class Solution:
    def networkDelayTime(self, times, n, k) -> int:
        edges = collections.defaultdict(list)
        
        def dijkstra(k):
            q = [(k, 0)]
            reached = {k: 0}
            while q:
                node, path_cost = heapq.heappop(q)

                for edge in edges[node]:
                    child, weight = edge
                    new_cost = path_cost + weight
                    if child not in reached or new_cost < reached[child]:
                        reached[child] = new_cost
                        heapq.heappush(q, (child, new_cost))
            
            reached.pop(k)          
            return reached
        
        for time in times:
            edges[time[0]].append((time[1], time[2]))
        
        reached_cost = dijkstra(k)
        
        maxim = 0
        for cost in reached_cost.values():
            maxim = max(maxim, cost)

        return maxim if len(reached_cost) == n - 1 else -1