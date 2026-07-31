class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = { i:[] for i in range(n) }

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visited = set()

        def dfs(i):
            visited.add(i)

            for neighbor in adjList[i]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res