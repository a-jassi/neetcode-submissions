class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = max(count.values())
        maxCount = 0
        for i in count.values():
            maxCount += 1 if i == maxFreq else 0
        
        time = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), time)