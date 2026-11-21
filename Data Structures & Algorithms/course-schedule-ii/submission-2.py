
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        ret = []
        for course, pre in prerequisites:
            preMap[course] += [pre]
        
        visited = set() 
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            
        
            if course in visited:
                return True

            

            cycle.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            ret.append(course)
            visited.add(course)
            cycle.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        
        return ret
            

            
        
        
        
        
