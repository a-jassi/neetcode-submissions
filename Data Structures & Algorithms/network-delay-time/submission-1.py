class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { i:[] for i in range(1, n + 1) }

        for u, v, t in times:
            adjList[u].append((v, t))

        pq = [(0, k)]
        visited = set()
        t = 0

        while pq:
            w, node = heapq.heappop(pq)
            if node in visited:
                continue
            
            visited.add(node)
            t = w

            for nei, wei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(pq, (w + wei, nei))
        
        return t if len(visited) == n else -1


