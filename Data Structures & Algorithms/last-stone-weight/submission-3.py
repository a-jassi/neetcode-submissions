class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stoneA = -heapq.heappop(stones)
            stoneB = -heapq.heappop(stones)

            diff = abs(stoneA - stoneB)
            if diff != 0:
                heapq.heappush(stones, -diff)
        
        return 0 if len(stones) == 0 else -stones[0]