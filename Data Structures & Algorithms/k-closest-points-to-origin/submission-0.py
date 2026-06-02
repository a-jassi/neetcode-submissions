class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(maxHeap, (-dist, p))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [p[1] for p in maxHeap]