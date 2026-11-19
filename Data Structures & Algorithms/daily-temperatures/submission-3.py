class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0 for i in range(len(temperatures))]

        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                ind = stack.pop()
                ret[ind] = i-ind
            stack.append(i)
            
        return ret