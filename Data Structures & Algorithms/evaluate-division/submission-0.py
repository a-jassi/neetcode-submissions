class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}

        # create adjList
        for i, eq in enumerate(equations):
            num, denom = eq
            if num not in adjList:
                adjList[num] = []
            if denom not in adjList:
                adjList[denom] = []
            
            adjList[num].append((denom, values[i]))
            adjList[denom].append((num, 1 / values[i]))
        
        def dfs(curr, dst, visited):
            if curr not in adjList or dst not in adjList:
                return -1
            if curr == dst:
                return 1
            
            visited.add(curr)

            for nei, val in adjList[curr]:
                if nei not in visited:
                    product = dfs(nei, dst, visited)
                    if product != -1:
                        return val * product
            return -1
        
        res = []
        for num, denom in queries:
            visited = set()
            product = dfs(num, denom, visited)
            res.append(product)

        return res
            



