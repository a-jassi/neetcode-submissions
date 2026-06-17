class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for neighbour in adjList[curr]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, curr):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n
        
            

        
        