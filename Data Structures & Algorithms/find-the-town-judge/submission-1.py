class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjList = defaultdict(int)
        for i in range(len(trust)):
            a, b = trust[i]
            adjList[a] -= 1
            adjList[b] += 1
        
        for i in range(1, n + 1):
            if adjList[i] == n - 1:
                return i
        return -1