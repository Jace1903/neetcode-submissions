import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))

        dist={node:float('inf')for node in range(1,n+1)}
        dist[k]=0
        pq=[(0,k)]
        while pq:
            d,u= heapq.heappop(pq)
            if d>dist[u]:
                continue
            for v,t in graph[u]:
                if d+t<dist[v]:
                    dist[v]=d+t
                    heapq.heappush(pq,(dist[v],v))
        ans=max(dist.values())
        return ans if ans<float('inf')else -1

        