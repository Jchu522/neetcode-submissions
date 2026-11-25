class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #backtracking with an index variable
        #we can do isPal with the string and the l and r 
        #just keep going though every substring
        
        ret = []
        subPal = []
        def backtrack(j, i):
            if i >= len(s):
                if i == j:
                    ret.append(subPal.copy())
                return 

            if self.isPali(s, j, i):
                subPal.append(s[j:i+1])
                backtrack(i+1, i+1)
                subPal.pop()
            
            backtrack(j, i+1)

        backtrack(0,0)
        return ret

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

        