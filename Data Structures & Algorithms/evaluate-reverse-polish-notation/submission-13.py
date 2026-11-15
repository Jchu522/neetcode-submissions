class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for temp in tokens:
            if temp == '*':
               stack.append(stack.pop() * stack.pop())
            elif temp ==  '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif temp == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            elif temp == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            else:
                stack.append(int(temp))
        return stack.pop()


