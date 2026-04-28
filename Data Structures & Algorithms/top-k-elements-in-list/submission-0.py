class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        freqs = []
        for num, count in freq_map.items():
            freqs.append((-count, num))
        
        heapq.heapify(freqs)

        res = []
        for _ in range(k):
            _, num = heapq.heappop(freqs)
            res.append(num)

        return res