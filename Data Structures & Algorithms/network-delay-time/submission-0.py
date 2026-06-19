class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { i:[] for i in range(n + 1) }
        for u, v, w in times:
            adjList[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            w, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            res = max(res, w)

            for neighbour, nWeight in adjList[node]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (nWeight + w, neighbour))
        
        return res if len(visited) == n else -1