class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we know how many parenthesis with n
        # you can only start with an opening parenthesis 
        # you can only have an closing parenthesis paired with opening
        # you can have an open and closing count where if open == closing == n
        
        ret = []
        stack = []

        def backtrack(opened, closed):
            if opened == closed == n:
                ret.append("".join(stack))
                return 
            
            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()
        
        backtrack(0,0)
        return ret
