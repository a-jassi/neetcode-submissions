class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = { i:[] for i in range(numCourses)}
        indegree = { i:0 for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        courseOrder = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            courseOrder.append(course)

            for c in adjList[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        return courseOrder if len(courseOrder) == numCourses else []