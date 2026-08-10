class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        degree = defaultdict(int)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque(i for i in range(n) if degree[i] == 1)
        remaining = n

        while remaining > 2:
            layer_size = len(queue)
            remaining -= layer_size

            for _ in range(layer_size):
                leaf = queue.popleft()
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)