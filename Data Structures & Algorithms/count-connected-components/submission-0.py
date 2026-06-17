class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i:[] for i in range(n) }

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(curr):
            if curr in visited:
                return
            
            visited.add(curr)
            for neighbour in adjList[curr]:
                dfs(neighbour)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res