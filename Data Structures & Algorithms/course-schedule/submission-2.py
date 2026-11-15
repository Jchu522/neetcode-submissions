

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre = {i:[] for i in range(numCourses)}
        for crs, prerec in prerequisites:
            pre[crs].append(prerec)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if pre[crs] == []:
                return True
            
            visitSet.add(crs)
            for prerec in pre[crs]:
                if not dfs(prerec): 
                    return False
            visitSet.remove(crs)
            pre[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True

