class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n + 1)}

        for src, dst, t in times:
            adjList[src].append((dst, t))
        
        pq = [(0, k)]
        visited = set()
        minTime = 0

        while pq:
            t1, n1 = heapq.heappop(pq)
            if n1 in visited:
                continue
            
            visited.add(n1)
            minTime = t1
            
            for nei, t2 in adjList[n1]:
                if nei not in visited:
                    heapq.heappush(pq, (t2 + t1, nei))
        
        return minTime if len(visited) == n else -1
