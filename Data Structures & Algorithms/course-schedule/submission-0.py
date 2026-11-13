

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre = {i: [] for i in range(numCourses)}
        for course, p in prerequisites:
            pre[course].append(p)
        
        visit = set()

        def dfs(course):

            if course in visit:
                return False

            if not pre[course]:
                return True
            
            visit.add(course)
            
            for p in pre[course]:
                if not dfs(p):
                    return False
            
            visit.remove(course)
            pre[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
                
        return True