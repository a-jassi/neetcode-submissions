class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = { i:[] for i in range(numCourses)}
        indegree = { i:0 for i in range(numCourses)}

        for pre, crs in prerequisites:
            adjList[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        coursesTaken = 0
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            coursesTaken += 1

            for c in adjList[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        return coursesTaken == numCourses