class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #val and index to calc diff
        res = [0 for i in range(len(temperatures))]
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                ind, temp = stack.pop()
                res[ind] = i - ind
            stack.append((i, val))

        return res
            

            