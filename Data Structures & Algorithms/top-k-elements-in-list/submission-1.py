class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        freqs = [[] for i in range(len(nums) + 1)]
        for num, count in freq_map.items():
            freqs[count].append(num)
        
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
