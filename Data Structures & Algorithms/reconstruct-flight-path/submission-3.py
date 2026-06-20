class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adjList = { src:[] for src, dest in tickets}
        for src, dest in tickets:
            adjList[src].append(dest)

        visited = set()
        res = ["JFK"]

        def dfs(curr):
            if len(visited) == len(tickets):
                return True
            if curr not in adjList:
                return False
            
            for i, neighbour in enumerate(adjList[curr]):
                if (curr, neighbour, i) in visited:
                    continue
                
                visited.add((curr, neighbour, i))
                res.append(neighbour)
                
                if dfs(neighbour):
                    return True

                visited.remove((curr, neighbour, i))
                res.pop()

            return False
        
        dfs("JFK")
        return res