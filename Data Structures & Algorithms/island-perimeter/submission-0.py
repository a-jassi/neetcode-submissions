class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(x, y):
            if x < 0 or x >= ROWS:
                return 1
            if y < 0 or y >= COLS:
                return 1
            if grid[x][y] == 0:
                return 1
            if (x, y) in visited:
                return 0
            
            visited.add((x, y))
            neighbours = (
                dfs(x + 1, y) +
                dfs(x - 1, y) + 
                dfs(x, y + 1) + 
                dfs(x, y - 1)
            )

            return neighbours
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    return dfs(x, y)
        
        return 0