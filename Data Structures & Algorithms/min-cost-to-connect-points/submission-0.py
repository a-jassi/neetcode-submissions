class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adjList = { i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((j, dist))
                adjList[j].append((i, dist))

        res = 0
        visited = set()
        minHeap = [(0, 0)]

        while len(visited) < n:
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            visited.add(node)
            res += dist

            for neighbour, distance in adjList[node]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (distance, neighbour))

        return res
