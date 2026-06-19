class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = { i:[] for i in range(len(edges) + 1) }
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(curr, prev):
            nonlocal cycleStart

            if curr in visited:
                cycleStart = curr
                return True
            
            visited.add(curr)
            for neighbour in adjList[curr]:
                if neighbour == prev:
                    continue
                if dfs(neighbour, curr):
                    if cycleStart != -1:
                        cycle.add(curr)
                    if curr == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []
