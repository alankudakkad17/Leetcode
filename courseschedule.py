class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[] for _ in range(numCourses)]
        indeg=[0]*numcourses
        for i,j in prerequisites:
            g[b].append(a)
            indeg[a]+=1
        q=[i for i,x in enumerate(indeg) if x==0]
        for i in q:
            numCourses -= 1  # Mark this course as completed
            for j in g[i]:    # For each course that depends on course i
                indeg[j] -= 1 # Reduce its prerequisite count
                if indeg[j] == 0:  # If all prerequisites are satisfied
                    q.append(j) 
