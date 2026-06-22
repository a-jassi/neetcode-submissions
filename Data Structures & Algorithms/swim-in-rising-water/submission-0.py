class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = [(grid[0][0], 0, 0)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            maxH, r, c = heapq.heappop(minHeap)
            if r == c == (len(grid) - 1):
                return maxH
            
            for dr, dc in directions:
                nRow, nCol = r + dr, c + dc
                if nRow < 0 or nRow >= len(grid):
                    continue
                if nCol < 0 or nCol >= len(grid):
                    continue
                if (nRow, nCol) in visited:
                    continue

                visited.add((nRow, nCol))
                newMax = max(maxH, grid[nRow][nCol])
                heapq.heappush(minHeap, (newMax, nRow, nCol))

